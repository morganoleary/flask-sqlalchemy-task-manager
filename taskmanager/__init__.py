# This file will make sure to initialize our taskmanager application as a package, allowing us to use
# our own imports, as well as any standard imports.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import package to use hidden environment variables - importing only if the file is found
if os.path.exists("env.py"):
    import env


# create an instance of imported Flask class
app = Flask(__name__) # takes default 'name' module
# specify 2 app configuration variables from the environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Then, we need to create an instance of the imported SQLAlchemy() class, which will be
# assigned to a variable of 'db', and set to the instance of our Flask 'app'.
db = SQLAlchemy(app)

# The reason this is being imported last, is because the 'routes' file, that we're about
# to create, will rely on using both the 'app' and 'db' variables defined above.
from taskmanager import routes