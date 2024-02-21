from flask import flash, redirect, render_template, request, Blueprint, abort,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user,logout_user
from my_app import db
from my_app.api.models import Task, User
from my_app.api.forms import RegisterForm, LoginForm, TodoForm,EditTodoForm
from my_app.middlewares.logger_config import setup_logger

todo = Blueprint('tasks', __name__)

# Set up logging configuration
logger = setup_logger(__name__)

@todo.route('/')
@todo.route('/home')
def home():
    logger.error('Home page accessed')
    return render_template('home.html')

@todo.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit:
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user:
                flash("User with this email already exists", "error")
                return render_template('register.html', form=form)
            
            user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        email=form.email.data,
                        password=generate_password_hash(form.password.data)
                        )
            db.session.add(user)
            db.session.commit()
            logger.info('New user registered: %s', user.email)
            return redirect('/login')

@todo.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            logger.info('User logged in: %s', user.email)
            return redirect('/todos')
        flash("Invalid email or password", "error")
            

    return render_template('login.html', form=form)

@todo.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect('/home')

@todo.route('/add_todo', methods=['POST', 'GET'])
def add_tasks():
    user = current_user
    form = TodoForm()
    if request.method == 'GET':
        return render_template('add_todo.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit:
            todo = Task(task_name=form.task_name.data, status=form.status.data,
                        due_date=form.due_date.data, todo_owner=user.id
                        )
            db.session.add(todo)
            db.session.commit()
            logger.info('New todo added by user %s: %s', user.email, todo.task_name)
            return redirect('/todos')

@todo.route('/todos')
def todos():
    todos = Task.query.filter_by(todo_owner=current_user.id)
    logger.info('Retrieved todos for user: %s', current_user.email)
    return render_template('todos.html', todos=todos)

@todo.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    user = current_user
    task = Task.query.filter_by(id=id, todo_owner=current_user.id).first()

    if task is None:
        logger.warning('Task with id %d not found for user %s', id, user.email)
        abort(404)

    form = EditTodoForm(request.form, obj=task)
    if request.method == 'POST' and form:
        form.populate_obj(task)
        db.session.commit()
        logger.info('Task edited by user %s: %s', user.email, task.task_name)
        return redirect('/todos')

    return render_template('edit_todo.html', form=form)

@todo.route('/delete_task/<int:id>', methods=['GET', 'POST'])
def delete(id):
    task = Task.query.filter_by(id=id, todo_owner=current_user.id).first()
    if request.method == 'POST':
        if task:
            db.session.delete(task)
            db.session.commit()
            logger.info('Task deleted by user %s: %s', current_user.email, task.task_name)
            return redirect('/todos')
        abort(404)

    return render_template('delete_task.html')