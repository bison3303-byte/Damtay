from flask import request, render_template, redirect
from . import app
from .library.systeminfo import *

@app.route("/", methods=["GET", "POST"])
def index():
    return redirect("/login", code=302)

@app.route("/login", methods=["GET", "POST"])
def login():

    if "GET" not in request.method:
        secretCode = request.form.get("code")
        return redirect("/dashboard", 301)
    return render_template("login.html")
    
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    
    return render_template("dashboard.html", cpuPercentage=sysinfo.cpuPerc(), ramPercentage=sysinfo.ramPerc(), osname = sysinfo.osFull())