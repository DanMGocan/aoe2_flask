# Data import #
from data import data_dict

# Custom imports #
from helper_functions import create_units, counter_unit

# Flask imports #
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/counter/troops/<string:unit_name>")
def counter_unit_view(unit_name):
    data = create_units()

    list_of_units = data.keys()
    if unit_name in list_of_units:
        counters = counter_unit(unit_name, data, None)
        return render_template("unit_counter", 
                            template_list_of_counters = counters,
                            template_unit_name = unit_name)
    else:
        return render_template("404.html")

@app.route("/counter/buildings/<string:building_name>")
def counter_building_view(building_name):
    pass
