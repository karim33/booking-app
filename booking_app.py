from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+pymysql://Booking-app:osman123@localhost:8889/Booking-app')
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
#app.secret_key = 'welloethio'


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(120))
    LastName = db.Column(db.String(120))
    Email = db.Column(db.String(120), unique=True)
    Address = db.Column(db.String(120))
    ServiceType = db.Column(db.String(220))
    #posts = db.relationship('Blog', backref='owner')

    def __init__(self, FirstName, LastName, Email, Address, ServiceType):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Address = Address
        self.ServiceType = ServiceType

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', ), 404

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')

@app.route("/")
@app.route('/home')
def index():
    return render_template('index.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/form")
def form():
    return render_template('form.html')


if __name__ == '__booking_app__':
	app.run()
