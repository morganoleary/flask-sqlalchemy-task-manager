# create database schema by defining models
from taskmanager import db

# create 2 tables represented by class-based models in the SQLAlchemy ORM
# use declarative base from SqlAlchemy's model
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # string has max. character count of 25 / make sure each new category is unique / & not empty or blank
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # link foreign key & cascade deletion from Task class (not visible on database) | ref. to 1-to-many rel.
    # "Task" point to the table being targeted | needs to backref itself (Category table)
    # cascade >> find all related tasks and delete them | lazy >> identify any task linked to the categories queried in database
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)


    # standarad Python function __repr__ = represents the class objects as a string
    def __repr__(self):
        # __repr__ to represent itself (like 'this') in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # Text instead of string allows longer strings to be used (like textareas vs inputs)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # to use time instead = db.DateTime or db.Time
    due_date = db.Column(db.Date, nullable=False)
    # ForeignKey points to the id category in the Category class
    # ondelete='CASCADE' | one to many relationship | when a category is deleted it performs a cascading effect
    # & also delete any task linked to it
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string

        # We could simply return self.task_name, but instead, let's utilize some of Python's formatting to include different columns.
        # We'll use placeholders of {0}, {1}, and {2}, and then the Python .format() method to specify
        #that these equate to self.id, self.task_name, and self.is_urgent.

        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )

