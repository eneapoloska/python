from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# HTML Template to login or register

@app.route('/loginPage')
def loginPage():
    if 'user_id' in session: # check if someone is loged in 
        return redirect('/')
    return render_template('loginRegister.html') # it rendesr the html file


#POST Method to create a User ex. Register
@app.route('/createUser', methods=['POST'])
def createUser():
    if not User.validate_user(request.form):
        flash('Somethings wrong ninja!', 'signUp')
        return redirect(request.referrer)
    
    if User.get_user_by_email(request.form):
        flash('My friend, this email already exists! What are you trying to do?!! Hack me?!', 'emailSignUp')
        return redirect(request.referrer)
        # data is an object that has everthing that the user table in our databese in order to be created 
    data = {
        'email': request.form['email'], # we create a key of email and we get it from the form at registratin, 
                                        #request.form['email'] is the email  we get from the input mail from name="email"
        'name': request.form['name'],
        'lastName': request.form['lastName'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    User.create_user(data) # we call a method here<<---- and sva
    return redirect('/')


#POST method to log the user in

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    if len(request.form['email'])<1:
        flash('Email is required to login', 'emailLogin')
        return redirect(request.referrer)
    if not User.get_user_by_email(data):
        flash('This email doesnt exist in this application', 'emailLogin')
        return redirect(request.referrer)

    user = User.get_user_by_email(data)###User.get_user_by_email is from the user.py the classmethod def.get_user_by_email(cls,data)

    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password", 'passwordLogin')
        return redirect(request.referrer)
        
    session['user_id'] = user['id']###after we save the user by email in user 
                                    #we stored the user id in sesion we create in session['user_id']
    return redirect('/')####

# Route to display the main page 
@app.route('/')
def dashboard():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }#we create a data object with the key user id wich we get from the session
        user = User.get_user_by_id(data)
        allPosts = Post.getAllPosts()#allPosts  is variable that saves everithong from Post.getAllPosts()
                                    #Pos is the class of Post '',getAllPosts() is a method we dont pass data we dont have e specific condition just get all the post  
        userLikedPosts = User.get_logged_user_liked_posts(data)
        return render_template('dashboard.html', loggedUser= user, allPosts = allPosts, userLikedPosts= userLikedPosts)
    return redirect('/logout')


#Route to display a specific user information
@app.route('/profile/<int:id>') # int=initiger the meaning of the nr of the id user 
def profile(id):
    if 'user_id' in session:
        data = {
            'user_id': id
        }
        user = User.get_user_by_id(data)
        posts = User.get_all_user_info(data)
        return render_template('profile.html', posts= posts, user= user)
    return redirect('/logout')

#Route to log the user out -- Clean the session

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/loginPage')