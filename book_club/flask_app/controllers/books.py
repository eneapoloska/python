from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.book import Book
from flask import flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import datetime
import uuid
import os
UPLOAD_FOLDER = 'flask_app/static/img/IMAGE_UPLOADS'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/createBook', methods=['POST'])
def createBook():

    if request.files['image'] == None:
        flash('Image is required', 'image')
        return redirect(request.referrer)
    elif request.files['image'] != None:
        image= request.files['image']
    if not Book.validate_book(request.form):
        return redirect(request.referrer)
    

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        time = datetime.now().strftime("%d%m%Y%S%f")
        time += filename
        filename = time
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'user_id': session['user_id'],
        'image': filename
    }
    book = Book.create_book(data)
    dataBook = {
        'book_id': book['id'],
        'user_id': session['user_id']
    }
    Book.addLike(dataBook)
    return redirect('/')

@app.route('/like/<int:id>') # every time we like a book 
def addLike(id):
    data = {
        'book_id': id,
        'user_id': session['user_id']
    }
    Book.addLike(data)
    return redirect(request.referrer)

@app.route('/unlike/<int:id>')
def removeLike(id):
    data = {
        'book_id': id,
        'user_id': session['user_id']
    }
    Book.removeLike(data)
    return redirect(request.referrer)

@app.route('/delete/<int:id>')
def destroyBook(id):
    data = {
        'book_id': id,
    }
    book = Book.get_book_by_id(data)
    if session['user_id']==book['user_id']:
        Book.deleteAllLikes(data)
        Book.destroyBook(data)
        return redirect('/')
    return redirect(request.referrer)

#Route to display a specific book information
@app.route('/book/<int:id>') # int=initiger the meaning of the nr of the id book 
def bookSinglePage(id):
    if 'user_id' in session:
        data = {
            'book_id': id,
            'user_id': session['user_id']
        }
        user = User.get_user_by_id(data)
        book = Book.get_book_by_id(data)
        usersWhoLiked = Book.getUserWhoLiked(data)
        userLikedBooks = User.get_logged_user_liked_books(data)
        return render_template('bookClub.html', book= book, user= user, userLikedBooks=userLikedBooks, usersWhoLiked=usersWhoLiked)
    return redirect('/logout')

@app.route('/update/<int:id>', methods=['POST'])
def updateSingleBook(id):
    if 'user_id' in session:
        data = {
            'book_id': id,
            'user_id': session['user_id'],
            'description': request.form['description']
        }
        user = User.get_user_by_id(data)
        book = Book.get_book_by_id(data)
        if session['user_id']==book['user_id']:
            if len(request.form['description'])<5:
                flash('Description should be at least 5 characters!', 'descriptionUpdate')
                return redirect(request.referrer)
            Book.updateBook(data)
            return redirect(request.referrer)
        return redirect(request.referrer)
    return redirect('/logout')