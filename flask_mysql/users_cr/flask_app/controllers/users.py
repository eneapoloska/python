from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
# from flask_app.models.friend import Friend
@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
    all_users=User.get_all()
    return render_template ('users.html', users=all_users)

@app.route('/users/new')
def createUserPage():
    return render_template ('createuser.html')

@app.route('/create/user', methods=['POST'])
def createUser():
    data={
        'firstname': request.form['firstname'],
        'lastname': request.form['lastname'],
        'email': request.form['email'],
    }
    User.createuser(data)
    return redirect ('/')