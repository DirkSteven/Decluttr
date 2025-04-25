from flask import Flask
from flask_sqlalchemy import SQLAlchemy   
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize app
app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = '4acfddcdf3e1362c239375a48b0ea52e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # This is where you specify the route for login

# User loader function (ensure the `User` model is imported from your models file)
from decluttr.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes after initializing the app and login manager
from decluttr import routes
