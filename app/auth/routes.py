from crypt import methods
from flask import Blueprint, render_template, request, redirect, flash, url_for

from app.auth.auth_forms import SignInForm, SignUpForm

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix = '/auth')

@auth.route('/', methods=['GET', 'POST'])
def signin():
    inform = SignInForm()
    if request.method == 'POST':
        if inform.validate_on_submit():
            flash(f'Hello, {inform.username.data}!')
            return redirect(url_for('home'))
        else:

            flash(f'Incorrect username or password.')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', inform=inform)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    upform = SignUpForm()
    if request.method == 'POST':
        if upform.validate_on_submit():
            return redirect(url_for('auth.signin'))
        else:
            flash('Please fill out required fields.')
            return redirect(url_for('auth.signup'))
    return render_template('signup.html', upform=upform)