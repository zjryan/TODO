from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(3,20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')