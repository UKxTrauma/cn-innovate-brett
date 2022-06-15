from flask import render_template, Blueprint

views = Blueprint('views', __name__)

# view in this instance is a Blueprint


@views.route('/')
def home():
    return render_template('index.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/about')
def about():
    return render_template('about.html')