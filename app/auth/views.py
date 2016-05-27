from . import auth
from .forms import LoginForm
from flask import render_template, redirect, request, url_for

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html',
                           form=form)