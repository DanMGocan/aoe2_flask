import requests
import time
from datetime import datetime
from extract_unit_links import all_units_links


links_url = []
for element in all_units_links.keys():
    for link in all_units_links[f"{element}"]:
        links_url.append(link)

print(links_url)


## Ping all unit links, to make sure the links are working 
# for element in links_url:

#     current_time = datetime.now()
    
#     try:
#         is_up = requests.get(element).status_code == 200
#         with open("logs/ping_results.json", "a", 1, "utf-8") as file:
#             file.write(f"URL at {element} was successfully pinged at {current_time}\n")

#     except:
#         with open("logs/ping_results.json", "a", 1, "utf-8") as file:
#             file.write(f"!!! ERROR at {element}! Was UNSUCCESSFULLY pinged at {current_time}\n")

