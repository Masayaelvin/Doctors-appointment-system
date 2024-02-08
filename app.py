from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, AppointmentForm, DoctorsRegistration, ServiceForm


app =  Flask(__name__)
app.config['SECRET_KEY'] = 'd3f771ce5d7a1fda2992ab10a9305214'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        flash(f'An account has been created for {form.FirstName.data}', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html',title='register', form=form)


@app.route('/Login',  methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)