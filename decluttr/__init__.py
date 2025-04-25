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
# Increase SQLite timeout to 15 seconds to handle potential locking issues
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {'timeout': 15}
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the route for login
login_manager.login_message_category = 'info'

# User loader function
from decluttr.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes after initializing the app and login manager
from decluttr import routes
