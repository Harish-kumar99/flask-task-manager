from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from my_app.middlewares.config_secret import SECRET_KEY



# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import blueprint after creating the app to avoid circular imports

from my_app.api.views import todo
app.register_blueprint(todo)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Import User model after creating the db
from my_app.api.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables within the application context
with app.app_context():
    db.create_all()
