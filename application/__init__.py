from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '82fcc1d59465a9b274d13db8441cbc30'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes



