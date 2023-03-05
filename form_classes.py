from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UnitCounter(FlaskForm):
    unit_name = StringField("Unit name")
    submit = SubmitField("Submit")