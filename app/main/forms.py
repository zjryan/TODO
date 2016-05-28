from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(Form):
    content = StringField('Task content', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Add task')