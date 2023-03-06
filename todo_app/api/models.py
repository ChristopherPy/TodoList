from todo_app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String)
    todos = db.relationship('Todo', backref='owner')

    def __repr__(self):
        return f'User: {self.first_name} {self.email}'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_name = db.Column(db.String(255))
    description = db.Column(db.String(1500))
    deadline = db.Column(db.DateTime())
    status = db.Column(db.String(255))
    todo_owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'ToDo: {self.todo_name} [{self.deadline}]'