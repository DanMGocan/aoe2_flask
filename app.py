# Data import #
from data import units_dict, buildings_dict, technologies_dict

# Custom imports #
from helper_functions import create_units, counter_unit

# Form classes imports #
from form_classes import *

# Flask imports #
from flask import Flask, render_template, request


app = Flask(__name__)
app.config["SECRET_KEY"] = "123456"

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/counter/troops/", methods=["GET", "POST"])
def counter_unit_view():
    data = create_units() # to be removed in production
    unit_counter_form = UnitCounter()
    unit_name = unit_counter_form.unit_name.data
    units = ["unit_1", "unit_2", "unit_3", "unit_4", "unit_5"]

    list_of_units = data.keys()

    # If unit is valid #
    if unit_name in list_of_units:
        return render_template("unit_counter.html", 
                            template_list_of_counters = counter_unit(unit_name, data, None),
                            template_unit_name = unit_name,
                            template_list_of_units = list_of_units,
                            template_form = unit_counter_form,
                            template_units = units)
    
    # If unit is not valid #
    elif unit_name and unit_name not in list_of_units:
        return render_template("404.html")

    # If no unit has been input yet #  
    else:
        return render_template("unit_counter.html",
                        template_form = unit_counter_form,
                        template_units = units,
                        template_list_of_units = list_of_units,
)


@app.route("/counter/buildings/<string:building_name>", methods=["GET", "POST"])
def counter_building_view(building_name):
    pass
