import requests
from bs4 import BeautifulSoup

url = 'https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires_II)'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'article-table'})
rows = table.find_all('tr')

units = {}

for row in rows[1:]:
    cells = row.find_all('td')
    if len(cells) >= 3:
        name = cells[0].text.strip().lower().replace(" ", "_")
        added_in = cells[1].text.strip().lower()
        description = cells[2].text.strip().lower()
        unit = {
            "name": name,
            "added_in": added_in,
            "description": description
        }
        if len(cells) >= 4:
            unit["type"] = cells[3].text.strip().lower()
        units[name] = unit

print(units)
