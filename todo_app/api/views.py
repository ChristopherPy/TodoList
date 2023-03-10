from flask import Blueprint, redirect, render_template, request, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from todo_app import db
from todo_app.api.models import User, Todo
from todo_app.api.forms import RegisterForm, LoginForm, TodoForm, EditTodoForm
todos = Blueprint('todos', __name__)


@todos.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect('/todos')

    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit:
            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        email=form.email.data,
                        password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            return redirect('/login')


@todos.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect('/todos')
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect('/todos')
        flash('Invalid email or password')
    return render_template('login.html', form=form)


@todos.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/login')


@todos.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    form = TodoForm()
    if request.method == 'GET':
        return render_template('add_todo.html', form=form)
    if request.method == 'POST':
        user = current_user
        if form.validate_on_submit:
            todo = Todo(todo_name=form.todo_name.data,
                        description=form.description.data,
                        deadline=form.deadline.data,
                        status=form.status.data,
                        todo_owner=user.id,
                        parent_id=None)
            db.session.add(todo)
            db.session.commit()
            return redirect('/todos')


@todos.route('/todos')
def todos1():
    if current_user.is_authenticated:
        todos1 = Todo.query.filter_by(
            todo_owner=current_user.id).filter(Todo.parent_id == None).all()
        return render_template('todos.html', todos1=todos1)
    else:
        return redirect('/login')


@todos.route('/edit_todo/<int:id>', methods=['GET', 'POST'])
def edit_todo(id):
    # user = current_user
    form = EditTodoForm()
    todo = Todo.query.filter_by(id=id, todo_owner=current_user.id).first()

    if request.method == 'POST':
        if form.submit.data:
            todo.todo_name = form.todo_name.data
            todo.description = form.description.data
            todo.deadline = form.deadline.data
            todo.status = form.status.data
            db.session.commit()
            return redirect('/todos')

    elif request.method == 'GET':
        form.todo_name.data = todo.todo_name
        form.description.data = todo.description
        form.deadline.data = todo.deadline
        form.status.data = todo.status
    return render_template('edit_todo.html', form=form, todo=todo)


@todos.route('/delete_todo/<int:id>', methods=['GET', 'POST'])
def delete(id):
    todo = Todo.query.filter_by(id=id, todo_owner=current_user.id).first()
    if request.method == 'POST':
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return redirect('/todos')
        abort(404)

    return render_template('delete_todo.html', todo=todo)


@todos.route('/add_subtodo/<int:id>', methods=['GET', 'POST'])
def add_subtodo(id):
    parent_todo = Todo.query.filter_by(
        id=id, todo_owner=current_user.id).first()
    form = TodoForm()
    if request.method == 'GET':
        return render_template('add_subtodo.html',
                               form=form,
                               parent_todo=parent_todo)
    if request.method == 'POST':
        user = current_user
        if form.validate_on_submit:
            subtodo = Todo(todo_name=form.todo_name.data,
                           description=form.description.data,
                           deadline=form.deadline.data,
                           status=form.status.data,
                           todo_owner=user.id,
                           parent_id=parent_todo.id)
            db.session.add(subtodo)
            db.session.commit()
            return redirect('/todos')
