from flask import  render_template, url_for, flash, redirect
from DAS.forms import RegistrationForm, LoginForm, AppointmentForm, DoctorsRegistration, ServiceForm
from flask_bcrypt import Bcrypt
import uuid
from DAS import app

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    from DAS.models import User, db
    form = RegistrationForm()
    if form.validate_on_submit():
        encrpted_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_id = str(uuid.uuid4())
        user = User(User_id=user_id, FirstName=form.FirstName.data, LastName=form.LastName.data, phone_number = form.phone_number.data, email=form.email.data, password=encrpted_pwd)
        flash(f'An account has been created for {form.FirstName.data} you can now log in' , 'success')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html',title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/appointment')
def appointment():
    form = AppointmentForm()
    return render_template('appointment.html', form=form)


@app.route('/doctors')
def doctors():
    form = DoctorsRegistration()
    return render_template('doctors.html', form=form)


@app.route('/services', methods=['POST', 'GET'])
def service():
    form = ServiceForm()
    return render_template('services.html', form=form)
