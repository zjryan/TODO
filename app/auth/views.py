from . import auth
from .forms import LoginForm, RegisterationForm
from ..models import User
from .. import db
from flask.ext.login import login_user, logout_user
from flask import render_template, redirect, url_for, flash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html',
                           form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data)
        u = User.query.filter_by(username=form.username.data).first()
        if u is not None:
            flash('This user is already exist.')
            redirect(url_for('auth.register'))
        else:
            db.session.add(user)
            flash('You have successfully registered.')
            return redirect(url_for('main.index'))
    return render_template('auth/register.html',
                           form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
