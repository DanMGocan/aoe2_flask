from extract_unit_links import all_units_links as unit_links
from helper_functions import UnitsDataExtractor

import requests
import time
from bs4 import BeautifulSoup
import pprint

all_units = {}

for building in unit_links:
    for url in unit_links[building]:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        parent_table = soup.find('aside')
        UnitsData = UnitsDataExtractor(parent_table)

        print(f"Extracting data from {url}")
        unit_info = {
            "name": UnitsData.get_name(),
            "added_in": UnitsData.get_added_in(),
            "type": UnitsData.get_type(),
            "civilization": UnitsData.get_civilization(),
            "age_available": UnitsData.get_age_available(),
            "trained_at": UnitsData.get_training_buildings(),
            "cost": UnitsData.get_cost(),
            "errors": UnitsData.errors_log,

        }

        all_units[unit_info["name"]] = unit_info



with open("units_db.py", "w") as f:
    f.write(pprint.pformat(all_units, indent=2, compact=False, depth=3, sort_dicts=False))
    f.close()


