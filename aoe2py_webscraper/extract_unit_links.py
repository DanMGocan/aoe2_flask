import requests
from bs4 import BeautifulSoup

# Link from where the units will be extracted #
generic_location = "https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires_II)"
unique_location = "https://ageofempires.fandom.com/wiki/Unique_unit_(Age_of_Empires_II)"
exceptions = ["wiki/unit_name", None]

def all_techs_extractor(generic_location, unique_location, exceptions):
    all_techs = {
        "Building_technologies": [],
        "Economy_technologies": [],
        "Monastery_technologies": [],
        "Military_technologies": [],
        "Dock": [],
        "Unique": []
    }

    
    new_request = requests.get(generic_location)
    soup = BeautifulSoup(new_request.content, "html.parser")

    for index, html_id in enumerate(list(all_techs.keys())):
        




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
            starting_point = soup.find(id=f'{html_id}').find_parent().find_next_sibling().find_next_sibling()

            for parent_list in starting_point.find_all("li"):
                for child_list in parent_list.find_all("a"):
                    if child_list.get("title"):
                        unit_link = child_list.get("href")
                        all_units[f"{html_id}"].append(f'https://ageofempires.fandom.com{unit_link}')
                    else:
                        continue 
                        
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
                        all_units["Castle"].append(f"https://ageofempires.fandom.com/{table_cells[1]['href']}")
        
    get_generic_units()
    get_unique_units()

    with open ("./logs/unit_links.js", "w") as f:
        f.write(str(all_units))
        f.close()

    return all_units

all_units_links = units_extractor(generic_location, unique_location, exceptions)

