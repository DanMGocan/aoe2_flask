from extract_unit_links import all_units_links as unit_links

import requests
import time
from bs4 import BeautifulSoup

all_units = {}

for building in unit_links:
    for url in unit_links[building]:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        parent_table = soup.find('aside')

        try:
            unit_info = {
                "name": parent_table.find("h2", {"class": "pi-title"}).text,
                "added_in": parent_table.find("div", {"data-source": "Intro"}).find("i").find("a").text,
                "type": parent_table.find("div", {"data-source": "Type"}).find("div").find("a").text,
                "civilization": parent_table.find("div", {"data-source": "Civilization"}).find("div").select_one("nth-child(1)").text

            }

            
            
            all_units[unit_info["name"]] = unit_info

        except:
            print(f"error at {url}")
            continue

with open("units_db.py", "w") as f:
    f.write(str(all_units))
    f.close()

