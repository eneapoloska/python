from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.magazine import Magazine
from flask import flash


@app.route('/createMagazine')
def createForm():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'user_id': session['user_id']
    }
    return render_template('addMagazine.html', loggedUser= User.get_user_by_id(data),)


@app.route('/create/magazine', methods = ['POST'])
def createMagazine():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Magazine.validate_magazine(request.form):
        return redirect(request.referrer)

    Magazine.create_magazine(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'magazine_id': id,
        'user_id': session['user_id']
    }
    currentMagazine = Magazine.get_magazine_by_id(data)

    if not session['user_id'] == currentMagazine['user_id']:
        flash('You cant delete this', 'noAccessError')
        return redirect('/dashboard')

    Magazine.delete(data)
    return redirect(request.referrer)


@app.route('/magazine/<int:id>')
def showOneMagazine(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'magazine_id': id,
        'user_id': session['user_id']
    }
    return render_template('showMagazine.html', loggedUser= User.get_user_by_id(data), magazine = Magazine.get_magazine_by_id(data))

@app.route('/edit/<int:id>')
def editForm(id):
    if 'user_id' not in session:
        return redirect('/logout')

    data = {
            'magazine_id': id,
            'user_id': session['user_id']
        }
        
    currentMagazine = Magazine.get_magazine_by_id(data)

    if not session['user_id'] == currentMagazine['user_id']:
        flash('You cant delete this', 'noAccessError')
        return redirect('/dashboard')

    return render_template('updateUser.html', loggedUser= User.get_user_by_id(data), magazine = Magazine.get_magazine_by_id(data))

@app.route('/update/<int:id>', methods = ['POST'])
def updateMagazine(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Magazine.validate_magazine(request.form):
        return redirect(request.referrer)
    
    currentMagazine = Magazine.get_magazine_by_id(request.form)

    if not session['user_id'] == currentMagazine['user_id']:
        flash('You cant delete this', 'noAccessError')
        return redirect('/dashboard')
    
    Magazine.update_magazine(request.form)

    return redirect('/')