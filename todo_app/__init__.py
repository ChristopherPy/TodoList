from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = "insert secret key"
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/index')
def home():
    return "Initial File"

with app.app_context():
    db.create_all()