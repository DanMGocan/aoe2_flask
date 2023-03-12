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
        mother_table = soup.find(attrs={"class": "fandom-table"}).find_all("tr")

        for table_row in mother_table:
            print(table_row.find_all("tr").find("td").find("a")[1]["href"])



        # for index, element in enumerate(mother_table):
        #     if element.find("td"):
        #         print(element.find_all("a")[1]("href"))
        #     else:
        #         continue 



    # get_generic_units()
    time.sleep(1)
    get_unique_units()

    return all_units

all_units_links = units_extractor(generic_location, unique_location, exceptions)
print(all_units_links)


# def units_extractor(links, exceptions):

#     all_units = []

#     for link in links:

#         # Creating the request and the BS object
#         new_request = requests.get(link)
#         soup = BeautifulSoup(new_request.content, "html.parser")

#         # Gathering all the attributes of a unit
#         result = soup.find_all("table", {"class" : "article-table"})
#         x = open("test1.py", "a")
#         x.write(result)
#         x.close()
        
#         for element in result:
#             for index, i in enumerate(element):
#                 for index, j in enumerate(i):
#                     for index, k in enumerate(j):
#                         try:
#                             unit_link = k.find("a")["href"]
#                             unit_full_link = f'https://ageofempires.fandom.com{unit_link} \n'
#                             if unit_link not in exceptions and unit_full_link not in all_units:
#                                 all_units.append(unit_full_link)
#                         except:
#                             pass
#         time.sleep(1)
    

#     return all_units

# all_unit_links = units_extractor(links, exceptions=[])

# f = open("all_unit_links.py", "a")
# for element in all_unit_links:
#     f.write(f'"{str(element)}"\n')
# f.close()