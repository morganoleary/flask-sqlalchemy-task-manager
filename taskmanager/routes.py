from flask import render_template # to use Flask functionality
from taskmanager import app, db # import from taskmanager package


# creat basic app route using root-level directory ( / ) to target function 'home'
@app.route("/")
def home():
    return render_template("base.html")
