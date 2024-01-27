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
    phone_number = IntegerField('phone number', 
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
    remember =BooleanField('Remember me')
    submit =SubmitField('Login')
    

class DoctorsRegistration(FlaskForm):
    Specialisation = StringField('Specilization', validators=[DataRequired()])
    Qualification = SelectField('Qualification', 
                                choices =[('sergon','sergion'), ('dentist', 'dentist'), ('gynacologist', 'gynacologist')], 
                                validators=[DataRequired(),Length(min=1)])
    Id_number = IntegerField('Nationa ID', validators=[DataRequired()])
    Availability = SelectField('availability', 
                               choices=[('always available', 'always available'), ('mon-fri', 'mon-fri'), 
                                        ('sat & sun','sat & sun' ),('currently not available!')],
                               validate_choice=True, validators=[DataRequired()])
    working_hours = StringField('working hours',validators=[DataRequired()] )
    Short_description = TextAreaField('Short_description')
    submit =SubmitField('Register')
    
    
class AppointmentForm(FlaskForm):
    appointment_date = DateField('Appointment Date', validators=[DataRequired()])
    appointment_time = TimeField('time',validators=[DataRequired()])
    doctors_name = StringField('Doctor')
    submit =SubmitField('Set appointment')
