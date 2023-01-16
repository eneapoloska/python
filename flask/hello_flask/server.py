from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key='skdfnlksdnfs875'
@app.route('/test')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    user=[{
        'name': 'enea', 
        'language': 'albanian',
    },
    {
        'name': 'endi', 
        'language': 'albanian',
    }]
    return render_template('hello.html', users=user)  # Return the string 'Hello World!' as a response

@app.route('/endi')          # The "@" decorator associates this route with the function immediately following
def hello_Endi():
    return 'Hello Endi!'  # Return the string 'Hello World!' as a response

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if 'user_id' in session:
        return redirect ('/home')
    return redirect('/logout')

# loginPage get 
@app.route('/loginPage')          # The "@" decorator associates this route with the function immediately following
def loginPage():
    if 'user_id' in session:
        return redirect ('/home')
    return render_template ('login.html')

#login the user POST
@app.route('/login', methods=['POST'])          # The "@" decorator associates this route with the function immediately following
def login():
    if 'user_id' in session:
        return redirect ('/home')
    session['user_id']=request.form['email']
    return redirect ('/home')

@app.route('/home')          # The "@" decorator associates this route with the function immediately following
def home():
    if 'user_id' in session:
        return render_template ('home.html', logeduser=session['user_id'])
    return redirect ('/logout')

@app.route('/logout')          # The "@" decorator associates this route with the function immediately following
def logout():
    session.clear()
    return redirect ('/loginPage')

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

@app.route('/table')
def render_table():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("table.html", users=users)

@app.route('/form_test')
def form():
    return render_template("form_test.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    #print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    #return redirect('/form_test')
    ##email = request.form['email']
    session['username'] = request.form['name']      # Here we add two properties to session to store the name and email
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html") #('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.