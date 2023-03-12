import requests
import time
from bs4 import BeautifulSoup

# Link from where the units will be extracted #
generic_location = "https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires_II)"
unique_location = "https://ageofempires.fandom.com/wiki/Unique_unit_(Age_of_Empires_II)"
exceptions = ["wiki/unit_name", None]

def units_extractor(generic_location, unique_location, exceptions):
    # Dictionary object using HTML IDs as keys 
    all_units = {
        "Barracks": [],
        "Archery_Range": [],
        "Stable": [],
        "Dock": [],
        "Siege_Workshop": [],
        "Town_Center": [],
        "Monastery": [],
        "Market": [],
        "Castle": [],
        "Dock": [],
        "Krepost": [],
        "Donjon": [],
        "Miscellaneous": []
    }

    def get_generic_units():
        new_request = requests.get(generic_location)
        soup = BeautifulSoup(new_request.content, "html.parser")
        for index, html_id in enumerate(list(all_units.keys())):
            # Getting the correct start location, by using the "id=dict_key as an anchor"
            starting_point = soup.find(id=f'{html_id}').find_previous().find_next_sibling().find_next_sibling("ul").find_all("li")
            for index, list_container in enumerate(starting_point):
                # Going throug every element in every <li> list to get the href of the unit
                unit_link = list_container.find_all("a")[1]["href"]

                if unit_link not in exceptions:
                    all_units[f'{html_id}'].append(unit_link)
    
    def get_unique_units():
        new_request = requests.get(unique_location)
        soup = BeautifulSoup(new_request.content, "html.parser")
        mother_table = soup.find(attrs={"class": "fandom-table"}).find("tbody").find_all("tr")

        for index, element in enumerate(list(mother_table)):
            all_row_data = list(element.find_all("td"))
            for index1, element1 in enumerate(all_row_data):
                if index1 == 1:
                    table_cells = list(element1.find_all("a"))
                    if len(table_cells) == 2:
                        all_units["Castle"].append(table_cells[1]['href'])
        
    get_generic_units()
    time.sleep(1)
    get_unique_units()

    return all_units

all_units_links = units_extractor(generic_location, unique_location, exceptions)
print(all_units_links)

