from flask import  render_template, url_for, flash, redirect, request
from DAS.forms import RegistrationForm, LoginForm, AppointmentForm, DoctorsRegistration, ServiceForm
from DAS.models import User, Doctor,Patient, Service, db
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
    form = RegistrationForm()
    if form.validate_on_submit():
        encrpted_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_id = str(uuid.uuid4())
        user = User(id=user_id, FirstName=form.FirstName.data, LastName=form.LastName.data, phone_number = form.phone_number.data, email=form.email.data, user_type= form.user_type.data, password=encrpted_pwd)
        db.session.add(user)
        db.session.commit()
        
        if form.user_type.data == 'Patient':
            patient = Patient(Patient_id=user.id, firstName=form.FirstName.data, lastName=form.LastName.data, phone_number = form.phone_number.data, email=form.email.data, user_type= form.user_type.data)
            db.session.add(patient)
            db.session.commit()
        else:
            return redirect(url_for('doctors'))
        
        flash(f'An account has been created for {form.FirstName.data} you can now log in' , 'success')
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
            next_page = request.args.get('next')
            if user.user_type == 'Doctor':
                flash(f'Welcome Doctor {form.email.data}!', 'success')
                doctor = Doctor.query.filter_by(email = current_user.email).first()
                Services = doctor.services
                if len(Services) == 0:
                    flash("you don't have any services yet please add a service to make your profile complete", "info")
                    return redirect(url_for('service'))
            else:
                flash(f'Welcome {form.email.data}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash(f'Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/user_type', methods=['GET', 'POST'])
def usertype():
    return render_template('usertype.html')


@app.route('/appointment', methods=['GET', 'POST'])
@login_required
def appointment():
    form = AppointmentForm()
    form.email.data = current_user.email
    
    return render_template('appointment.html', form=form)


@app.route('/doctors', methods=['GET', 'POST'])
def doctors():
    form = DoctorsRegistration()
    if form.validate_on_submit():
        doc = User.query.filter_by(email=form.email.data).first()
        doctor = Doctor(Doctor_id=doc.id, firstName=doc.FirstName, lastName=doc.LastName, license_number=form.license_number.data, clinic_name=form.clinic_name.data, clinic_address=form.clinic_address.data, email=form.email.data, working_hours=form.working_hours.data, Short_description=form.Short_description.data)
        db.session.add(doctor)
        db.session.commit()
        flash(f'Your details have been updated succesfully' , 'success')
        return redirect(url_for('login'))
        
    return render_template('doctors.html', form=form)


@app.route('/services', methods=['POST', 'GET'])
def service():
    form = ServiceForm()
    if form.validate_on_submit():
        flash(f'Your service {form.services.data} has been updated succesfully' , 'success')
        service_id  = str(uuid.uuid4())
        doc_id = Doctor.query.filter_by(Doctor_id = current_user.id).first().Doctor_id
        service = Service(service_id = service_id, doctor_id = doc_id, service_name = form.services.data)
        db.session.add(service)
        db.session.commit()
          
    return render_template('services.html', form=form)

@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
    return render_template('account.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))