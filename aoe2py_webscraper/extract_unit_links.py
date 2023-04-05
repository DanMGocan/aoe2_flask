import requests
from bs4 import BeautifulSoup

# Links from where the data will be extracted #
# gl = generic location # ul = unique location
units_gl = "https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires_II)"
units_ul = "https://ageofempires.fandom.com/wiki/Unique_unit_(Age_of_Empires_II)"
units_exceptions = ["wiki/unit_name", None]

tech_gl = "https://ageofempires.fandom.com/wiki/Technology_(Age_of_Empires_II)"
tech_ul = "https://ageofempires.fandom.com/wiki/Unique_technology"
tech_exceptions = ""

civs_gl = ""

def all_techs_extractor(generic_location, unique_location, exceptions):

    all_techs = {
        "Building_technologies": [],
        "Economy_technologies": [],
        "Monastery_technologies": [],
        "Military_technologies": {
            "Infantry": [],
            "Missile_/_siege": [],
            "Cavalry": [],
        },
        "Dock_technologies": []   
    }

    all_civs = []
    

    def get_generic_techs():

        new_request = requests.get(generic_location)
        soup = BeautifulSoup(new_request.content, "html.parser")

        # Function that would extract all the links
        def extract_links(starting_point, type_of_tech, military):
            for row in starting_point.find_all("tr")[1:]:
                tech_link = row.find("td").find("a", {"title": True}).get("href")

                if military:
                    all_techs["Military_technologies"][f'{type_of_tech}'].append(f"https://ageofempires.fandom.com{tech_link}")
                else:
                    all_techs[f'{type_of_tech}'].append(f"https://ageofempires.fandom.com{tech_link}")

        for index, html_id in enumerate(list(all_techs.keys())):

            if html_id == "Military_technologies": 
                for index, unit_type in enumerate(list(all_techs["Military_technologies"].keys())):
                    starting_point = soup.find(id=f"{unit_type}").find_parent().find_next_sibling("table", attrs={"class": "wikitable"}).find("tbody")
                    extract_links(starting_point, unit_type, True)

            else:
                starting_point = soup.find(id=f"{html_id}").find_parent().find_next_sibling("table", attrs={"class": "wikitable"}).find("tbody")
                extract_links(starting_point, html_id, False)

                # for table_data in starting_point:
                #     pass#print(table_data[0])

    def get_unique_techs():

        all_techs["Unique"] = []

        new_request = requests.get(unique_location)
        soup = BeautifulSoup(new_request.content, "html.parser")

        starting_point = soup.find("table", {"class": "fandom-table"}).find("tbody").find_all("tr")

        for index, row in enumerate(starting_point[1:]):

            if index % 2 == 0:

                civilization_link = row.find("td").select_one("a:nth-child(2)").get("href")
                tech_link = row.select_one("td:nth-child(2)").select_one("a:nth-child(2)").get("href")
                all_techs["Unique"].append(f"https://ageofempires.fandom.com{tech_link}")
                all_civs.append(f"https://ageofempires.fandom.com{civilization_link}")

            else:
                tech_link = row.find("td").select_one("a:nth-child(2)").get("href")
                all_techs["Unique"].append(f"https://ageofempires.fandom.com{tech_link}")

                


    get_generic_techs()
    get_unique_techs()
    return all_techs, all_civs

all_techs_links = all_techs_extractor(tech_gl, tech_ul, tech_exceptions)



def units_extractor(generic_location, unique_location, exceptions, techs, civs):

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
                        unit_link = table_cells[1]['href']
                        all_units["Castle"].append(f"https://ageofempires.fandom.com/{unit_link}")
        
    get_generic_units()
    get_unique_units()

    with open ("./logs/unit_links.js", "w") as f:
        f.write(str(all_units))
        f.close()

    return all_units

all_units_links = units_extractor(units_gl, units_ul, units_exceptions, all_techs_links[0], all_techs_links[1])

