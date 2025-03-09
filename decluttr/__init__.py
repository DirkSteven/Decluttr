from flask import Flask
from flask_sqlalchemy import SQLAlchemy   
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate



app = Flask(__name__)

app.config['SECRET_KEY'] = '4acfddcdf3e1362c239375a48b0ea52e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)



from decluttr import routes



