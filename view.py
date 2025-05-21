from app import app 
from flask import render_template
from markupsafe import escape

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login")
def loginpage():
    return render_template("login.html")
