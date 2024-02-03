from flask import Flask
from flask_mail import Mail, Message
from models import Appointment

app = Flask(__name__)
mail = Mail(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'Noreply-email@gmail.com'  # Update with your Gmail address
app.config['MAIL_PASSWORD'] = 'opiyomasaya'         # Update with your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'noreply.healthconnect@gmail.com'

# Dummy appointment data (replace with your actual data)
appointment = Appointment()
appointment.appointment_id = '123456'
appointment.service = 'Consultation'
appointment.appointment_date = '2024-02-01'
appointment.appointment_time = '10:00 AM'
appointment.appointment_status = 'Confirmed'

# Render the email content using the appointment data
email_content = f"""
                Greetings!
                Your appointment request has been submitted successfully!

                Appointment id: {appointment.appointment_id}
                Appointment date: {appointment.appointment_date}
                Appointment time: {appointment.appointment_time}
                Service: {appointment.service}
                Appointment status: {appointment.appointment_status}
                """

# Create the email message
msg = Message(subject='Appointment Request',
              recipients=['gabbynyangor@gmail.com'],  # Replace with recipient email address
              body=email_content)

# Send the email
try:
    with app.app_context():
        mail.send(msg)
    print('Email sent successfully!')
except Exception as e:
    print(f'Error sending email: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)
