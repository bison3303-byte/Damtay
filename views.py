from flask import request, render_template, Blueprint
from . import app
from .library.systeminfo import *
import psutil, platform

@app.route("/login", methods=["GET", "POST"])
def login():

    if "GET" not in request.method:
        secretCode = request.form.get("code")
        return redirect("/dashboard", 301)
    return render_template("login.html")
    
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    
    return render_template("dashboard.html", cpuPercentage=sysinfo.cpuPerc(), ramPercentage=sysinfo.ramPerc(), osname = sysinfo.osFull())