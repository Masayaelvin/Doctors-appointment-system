from flask import  render_template, url_for, flash, redirect
from DAS.forms import RegistrationForm, LoginForm, AppointmentForm, DoctorsRegistration, ServiceForm
from DAS.models import User
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import uuid
from DAS import app

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    from DAS.models import User, db
    form = RegistrationForm()
    if form.validate_on_submit():
        encrpted_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_id = str(uuid.uuid4())
        user = User(id=user_id, FirstName=form.FirstName.data, LastName=form.LastName.data, phone_number = form.phone_number.data, email=form.email.data, password=encrpted_pwd)
        flash(f'An account has been created for {form.FirstName.data} you can now log in' , 'success')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html',title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user =User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome {form.email.data}!', 'success')
            return redirect(url_for('account'))
        else:
            flash(f'Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/appointment', methods=['GET', 'POST'])
def appointment(): 
    form = AppointmentForm()
    return render_template('appointment.html', form=form)


@app.route('/doctors', methods=['GET', 'POST'])
def doctors():
    form = DoctorsRegistration()
    if form.validate_on_submit():
        flash(f'Your details have been updated' , 'success')
        
    return render_template('doctors.html', form=form)


@app.route('/services', methods=['POST', 'GET'])
def service():
    form = ServiceForm()
    if form.validate_on_submit():
        flash(f'Your service {form.services.data} has been updated' , 'success')
        
        
    return render_template('services.html', form=form)

@app.route('/account', methods=['POST', 'GET'])
def account():
    return render_template('account.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))