from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, IntegerField, BooleanField,
                     SelectField, TextAreaField, DateField, TimeField)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class RegistrationForm(FlaskForm):
    FirstName = StringField('First Name', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('Last Name', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    phone_number = StringField('phone number', 
                                validators=[DataRequired(), Optional()])
    password = StringField('Password', 
                           validators=[DataRequired(), Length(min=4, max=16, message="length of 4 and 16 characters")])
    confirm_password = StringField('Confirm Password',
                                   validators=[DataRequired(), EqualTo('password')])
    submit =SubmitField('Sign up')
    

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = StringField('Password', 
                           validators=[DataRequired(), Length(min=4, max=16, message="length of 4 and 16 characters")])
    remember =BooleanField('Remember Me')
    submit =SubmitField('Log In')
    

class DoctorsRegistration(FlaskForm):
    Qualification = SelectField('Specialization', 
                                choices =[('Doctor','Doctor'), ('surgeon', 'surgeon'), ('nurse', 'nurse')],
                                validators=[DataRequired()])
    Specialisation= SelectField('Qualification', 
                                choices =[('dermatologist','dermatologist'), ('dentist', 'dentist'), ('gynaecologist', 'gynaecologist')], 
                                validators=[DataRequired(),Length(min=1)])
    license_number = StringField('Licence Number', validators=[DataRequired()])
    clinic_name = StringField('Clinic Name', validators=[DataRequired(), Length(max=20)])
    clinic_address = StringField('Clinic Address', validators=[DataRequired(), Length(max=20)])
    working_hours = SelectField('working hours', 
                               choices=[('8-10', '8-10'), ('10-1', '10-1'), ('2-4','2-4')],
                               validate_choice=True, validators=[DataRequired()])
    availability = SelectField('Availability',
                               choices=[('currently not available!', 'currently not available!' ), ('available', 'available')],
                               validate_choice=True,
                               validators=[DataRequired()] )
    Short_description = TextAreaField('Short_description')
    submit =SubmitField('Add details')

class ServiceForm(FlaskForm):
    services = StringField('Add a service', validators=[DataRequired()] )
    submit = SubmitField('Add')
    
    
class AppointmentForm(FlaskForm):
    appointment_date = DateField('Appointment Date', validators=[DataRequired()])
    appointment_time = TimeField('time',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    service = SelectField('Service', choices=[('teeth removal', 'teeth removal'),('teeth removal', 'teeth removal') ,('teeth removal', 'teeth removal') ])
    doctor_name = StringField('Doctor')
    submit =SubmitField('Book Appointment')
