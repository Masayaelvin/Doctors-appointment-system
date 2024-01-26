from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from forms import RegistrationForm


app =  Flask(__name__)
app.config['SECRET_KEY'] = 'd3f771ce5d7a1fda2992ab10a9305214'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/registration')
def registration():
    form = RegistrationForm
    return render_template('registration.html', form=form)