from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'd3f771ce5d7a1fda2992ab10a930521'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()
db = SQLAlchemy(app)



from DAS import routes
