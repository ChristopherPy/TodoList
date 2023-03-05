from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


SECRET_KEY = "insert secret key"
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)


from todo_app.api.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/index')
def home():
    return "Initial File"

