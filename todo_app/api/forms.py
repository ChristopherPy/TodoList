from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class TodoForm(FlaskForm):
    todo_name = StringField('Name', validators=[DataRequired()])
    deadline = DateField('Deadline', validators=[DataRequired()])
    status = SelectField('Status', choices = [('Complete', 'Complete'), ('Not Started', 'Not Started')])
    submit = SubmitField('Add Todo')

class EditTodoForm(FlaskForm):
    todo_name = StringField('Name', validators=[DataRequired()])
    deadline = DateField('Deadline', validators=[DataRequired()])
    status = SelectField('Status', choices = [('Complete', 'Complete'), ('Not Started', 'Not Started')])
    submit = SubmitField('Edit Todo')