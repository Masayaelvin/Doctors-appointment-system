from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm, AppointmentForm, DoctorsRegistration

#flask is boring
app =  Flask(__name__)
app.config['SECRET_KEY'] = 'd3f771ce5d7a1fda2992ab10a9305214'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm
    return render_template('registration.html', form=form)


@app.route('/Login',  methods=['GET', 'POST'])
def Login():
    form = LoginForm
    return render_template('login.html', form=form)

@app.route('/appoinment')
def appointment():
    form = AppointmentForm
    return render_template('appointment.html', form=form)


@app.route('/Doctors')
def doctors():
    form = DoctorsRegistration
    return render_template('doctors.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)