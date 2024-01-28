from flask import render_template # to use Flask functionality
from taskmanager import app, db # import from taskmanager package
# import classes from models.py in order to generate our database
from taskmanager.models import Category, Task

# creat basic app route using root-level directory ( / ) to target function 'home'
@app.route("/")
def home():
    return render_template("tasks.html") # tasks is homepage
