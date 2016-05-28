from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')


class RegisterationForm(Form):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(4, 20),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters,'
                                                          'numbers, dots or underscores.')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2',
                                                                             message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')