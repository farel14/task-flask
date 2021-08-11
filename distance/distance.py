from flask import Blueprint, render_template

distance = Blueprint('distance', __name__, static_folder='static', template_folder='templates')

@distance.route('/home')
@distance.route('/')
def home():
    return render_template('home.html')