from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
# from flask_app.models.friend import Friend

@app.route('/')
def index():
    return render_template ('create.html')

@app.route('/allusers')
def showallusers():
    allUsers = User.get_allUsers()
    return render_template ('read.html', users = allUsers ) # users eshte tek jinja2 tek read.html, ku kemi user in users ?!?!?!?!?!??!?!?

@app.route('/usernew', methods=['POST'])
def createUser():
    data={
        'first_name': request.form['first_name'],# name from the form
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.createuser(data)
    return redirect ('/allusers')