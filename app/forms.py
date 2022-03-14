from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    pokename = StringField('Type Pokemon Name', validators = [DataRequired()])
    submit = SubmitField()


