import requests
from bs4 import BeautifulSoup

url = "https://ageofempires.fandom.com/wiki/Unique_unit_(Age_of_Empires_II)"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find the table with the class "fandom-table"
table = soup.find("table", {"class": "fandom-table"})

# Find the tbody tag in the table (if it exists)
tbody = table.find("tbody")

# Loop through all the tr tags in the table (or tbody)
for tr in tbody.find_all("tr"):
    # Find the second td tag in the row
    print(tr.find_all("td"))


    # Find the second a tag in the td tag
    #link = td.find_all("a")[1]

    # Extract the link's text and URL
    # print("Text: " + link.text)
    # print("URL: " + "https://ageofempires.fandom.com" + link['href'])
