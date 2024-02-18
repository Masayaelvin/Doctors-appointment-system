from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'd3f771ce5d7a1fda2992ab10a930521'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'noreply-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'yvud tirm yonc tfbf'         
app.config['MAIL_DEFAULT_SENDER'] = 'noreply.healthconnect@gmail.com'

from DAS import routes