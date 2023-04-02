# Using functions to extract the data, as we need to check for errors and issues #

from os import error
import re
from bs4 import BeautifulSoup



# Self explanatory #

class UnitsDataExtractor:
    # Variable to hold all the errors #

    def __init__(self, soup):
        self.soup = soup
        self.errors_log = {}

    def get_name(self):
        try:
            return self.soup.find("h2", {"class": "pi-title"}).text
        except Exception as e:
            self.errors_log["NameError"] = str(e)

    def get_added_in(self):
        try:
            return self.soup.find("div", {"data-source": "Intro"}).find("i").find("a").text
        except Exception as e:
            self.errors_log["AddedInError"] = str(e)

    def get_type(self):
        try:
            if (self.soup.find("div", {"data-source": "Type"}).find("div").find("a").text):
                return self.soup.find("div", {"data-source": "Type"}).find("div").find("a").text
            else:
                return "Generic"
        except Exception as e:
            self.errors_log["TypeError"] = str(e)

    def get_civilization(self):

        try:
            check_for_generic = self.soup.find("div", {"data-source": "Civilization"}).find("div", {"class": "pi-data-value"}).text
            number_of_civilizations = self.soup.find("div", {"data-source": "Civilization"}).find("div", {"class": "pi-data-value"}).find_all("a", {"title": True})
            list_of_civilizations = []

            if len(number_of_civilizations) == 0 or "All" in check_for_generic:
                return "Generic"
            else:
                for element in number_of_civilizations:
                    list_of_civilizations.append(element.text)
                
                return list_of_civilizations
                
        except Exception as e:
            self.errors_log["CivError"] = e

    def get_age_available(self):
        try:
            return self.soup.find("div", {"data-source": "Age"}).find("div", {"class": "pi-data-value"}).select_one(":nth-child(2)").text
        except Exception as e:
            self.errors_log["AgeError"] = str(e)

    def get_training_buildings(self):

        try: 
            main_building = self.soup.find("div", {"data-source": "Building"}).find("div", {"class": "pi-data-value"}).select_one(":nth-child(2)").text

            if len((self.soup.find("div", {"data-source": "Building"}).find("div", {"class": "pi-data-value"})).find_all(recursive=False)) <= 2:
                return [main_building]
            
            else:
                try:
                    secondary_building = self.soup.find("div", {"data-source": "Building"}).find("div", {"class": "pi-data-value"}).find("span").select_one(":nth-child(2)").text
                    return [main_building, secondary_building]
                except:
                    secondary_building = self.soup.find("div", {"data-source": "Building"}).find("div", {"class": "pi-data-value"}).select_one(":nth-child(4)").text
                    return [main_building, secondary_building]
                
        except Exception as e:
            self.errors_log["TrainBuildingError"] = e

    def get_cost(self):

        # Food cost #
        try:
            food_container = self.soup.find("div", {"data-source": "Food"}).find("div", {"class": "pi-data-value"})
            if len(food_container.find_all("span")) > 0:
                if len(food_container.find_all("span")) == 4: # exception added for Plumed Archer
                    food = food_container.select_one(":nth-child(2)").text
                else:
                    food = food_container.find("span").text
            else:
                food = food_container.text
        except:
            food = 0

        # Wood cost #
        try:
            wood_container = self.soup.find("div", {"data-source": "Wood"}).find("div", {"class": "pi-data-value"})
            if len(wood_container.find_all("span")) > 0:
                if len(wood_container.find_all("span")) == 4: # exception added for Plumed Archer
                    wood = wood_container.select_one(":nth-child(2)").text
                else:
                    wood = wood_container.find("span").text
            else:
                wood = wood_container.text
        except:
                wood = 0

        # Gold cost #
        try: 
            gold_container = self.soup.find("div", {"data-source": "Gold"}).find("div", {"class": "pi-data-value"})
            if len(gold_container.find_all("span")) > 0:
                if len(gold_container.find_all("span")) == 4: # exception added for Plumed Archer
                    gold = gold_container.select_one(":nth-child(2)").text
                else:
                    gold = gold_container.find("span").text
            else:
                gold = gold_container.text
        
        except:
            gold = 0

        cost = {
            "food": 0 if food == 0 else int(food.replace(",", "")),
            "wood": 0 if wood == 0 else int(wood.replace(",", "")),
            "gold": 0 if gold == 0 else int(gold.replace(",", ""))
        }

        return cost

        # except Exception as e:
        #     self.errors_log["CostError"] = str(e)



