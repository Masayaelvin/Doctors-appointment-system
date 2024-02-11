from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'd3f771ce5d7a1fda2992ab10a930521'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from DAS import routes