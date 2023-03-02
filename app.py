# Data import #
from data import data_dict

# Custom imports #
from helper_functions import calculate_unit_counter 

# Flask imports #
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route("/test")
def test():
    return data_dict.units

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/counter/troops/<string:unit_name>")
def counter_unit(unit_name):
    data = False
    calculate_unit_counter(unit_name, data)

