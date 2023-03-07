from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, \
      DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Sign In')


class TodoForm(FlaskForm):
    todo_name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    deadline = DateField('Deadline', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Complete', 'Complete'),
                                            ('Not Started', 'Not Started')])
    submit = SubmitField('Add Todo')


class EditTodoForm(FlaskForm):
    todo_name = StringField('Name', validators=[Optional()])
    description = TextAreaField('Description', validators=[Optional()])
    deadline = DateField('Deadline', validators=[Optional()])
    status = SelectField('Status', choices=[('Complete', 'Complete'),
                                            ('Not Started', 'Not Started')])
    submit = SubmitField('Edit Todo')
