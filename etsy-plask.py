from flask import Flask, render_template
APP = Flask(__name__)

@APP.route('/')
def home():
    return render_template('index.html')

@APP.route('/about')
def about():
    return render_template('about.html')
@APP.route('/contact')
def contact():
    return render_template('contact.html')
