from DAS import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous.url_safe import URLSafeSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(), primary_key=True)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.String(20))
    password = db.Column(db.String(60), nullable=False)
    
    def get_reset_token(self):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"user( username:'{self.FirstName}' '{self.LastName}' number: '{self.phone_number}' id:'{self.id}')"
    
# Association Table
doctor_patient_association = db.Table(
    'doctor_patient_association',
    db.Column('doctor_id', db.String, db.ForeignKey('doctor.Doctor_id')),
    db.Column('patient_id', db.String, db.ForeignKey('patient.Patient_id'))
)
                    
class Doctor(db.Model):
    Doctor_id = db.Column(db.String(), primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    license_number = db.Column(db.Integer, unique=True, nullable=False)
    qualification = db.Column(db.String(20), nullable=False)
    specialization = db.Column(db.String(20), nullable=False)
    clinic_name = db.Column(db.String(20), nullable=False)
    clinic_address = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.String(10), default='Doctor')  # Fixed the typo here
    working_hours = db.Column(db.String, nullable=False)
    Short_description = db.Column(db.Text)  # Corrected from db.column to db.Column
    services = db.relationship('Service', backref='doctor', lazy=True)
    patients = db.relationship('Patient', secondary=doctor_patient_association, backref='doctors', lazy=True)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    Appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    
    def __repr__(self):
        return f"Doctor( Doctor:'{self.firstName}' '{self.lastName}')"


class Patient(db.Model):
    Patient_id = db.Column(db.String(), primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.String(20), default='Patient')
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    Patient=db.relationship('Appointment' ,backref='client', lazy=True)
   
    def __repr__(self):
        return f"Patient( username:'{self.firstName}' '{self.lastName}' number:'{self.phone_number}' id:'{self.email}')"
    
    
                    
class Service(db.Model):
    service_id = db.Column(db.String(), primary_key=True)
    doctor_id = db.Column(db.String(), db.ForeignKey('doctor.Doctor_id'), nullable=False)
    service_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Service( service:'{self.service_id}' '{self.doctor_id}' service:'{self.service_name}')"

class Appointment(db.Model):
    appointment_id = db.Column(db.String(), primary_key=True, nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    appointment_time=db.Column(db.String, default='8-10')
    Doctor_id = db.Column(db.String(), db.ForeignKey('doctor.Doctor_id'), nullable=False)
    client_id = db.Column(db.String(),db.ForeignKey('patient.Patient_id'), nullable=False)
    service = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f"appointment( appointment:'{self.appointment_date}' '{self.appointment_time}' service:'{self.service}')"
    
    
db.drop_all()
db.create_all()