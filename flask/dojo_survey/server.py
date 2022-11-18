from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="589Wl@?97ga69opln5!#"

@app.route('/')
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def results():
    if len(request.form["name"])<1:
        flash("Please tell us your name")
        return redirect("/")
    if len(request.form["comments"])>180:
        flash("Write your comment whith less than 180 characters")
        return redirect("/")
    else:
        name = request.form["name"]
        dojo_location = request.form["dojo_location"]
        favlang = request.form["favlang"]
        comments = request.form["comments"]
        return render_template("result.html", name = name, dojo_location = dojo_location, favlang = favlang, comments = comments)

if __name__=="__main__":    
    app.run(debug=True)