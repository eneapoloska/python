from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
# from flask_app.models.friend import Friend
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/users')
    return redirect ('/logout')

@app.route('/loginPage')
def loginPage():
    if 'user_id' in session:
        return redirect('/users')
    return render_template('loginRegister.html')

@app.route('/login', methods=['POST'])
def login():
    if not User.getUserByEmail(request.form):
        flash('Email is not correct', 'emailLogin')
        return redirect(request.referrer)
    user = User.getUserByEmail(request.form)
    session['user_id'] = user['id']
    return redirect('/')

@app.route('/users')
def users():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'user_id': session['user_id']
    }
    return render_template ('users.html', users=User.get_all(), loggedUser = User.getUserById(data) )

@app.route('/create/user', methods=['POST'])
def createUser():
    if 'user_id' in session:
        return redirect('/')

    if not User.validate_user(request.form):
        return redirect(request.referrer)
    
    data={
        'firstname': request.form['firstname'],
        'lastname': request.form['lastname'],
        'email': request.form['email'],
    }
    User.createuser(data)
    flash('User created succesfully! You can login now!', 'userCreated')
    return redirect (request.referrer)

@app.route('/updateForm/<int:id>')
def updateForm(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if session['user_id'] != id:
        return redirect('/')
    data = {
        'user_id':id
    }
    return render_template ('updateUser.html', user = User.getUserById(data))

@app.route('/updateUser/<int:id>', methods=['POST'])
def updateUser(id):
    if session['user_id'] != id:
        return redirect('/')
    data={
        'firstname': request.form['firstname'],
        'lastname': request.form['lastname'],
        'email': request.form['email'],
        'user_id': id
    }
    User.updateUser(data)
    return redirect ('/')

@app.route('/delete/<int:id>')
def deleteUser(id):
    data ={
        'user_id' : id
    }
    User.delete_user(data)
    return redirect(request.referrer)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/loginPage')