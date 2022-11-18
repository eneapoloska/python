from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key='q987@89898Pku?'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def counter():
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    return render_template ('index.html')

@app.route('/delete_session')        
def reset():
    session.clear()
    return redirect ('/')

@app.route('/count', methods=['POST'])         
def plus2visits():
    if request.form['emri']=='add':
        session['count']+=1
    elif request.form['emri']=='reset':
        session['count']=0
    return redirect ('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode