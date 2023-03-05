# Function that calculates what unit counters the input unit best #

import random

# Function that creates a number of made-up units, to serve in testing #
def create_units():
    units = {}
    types = ["melee", "pierce"]
    civilizations = ["britons", "aztecs", "franks", "goths"]

    for i in range(1, 10):

        unit_dict = {
            "name": f"unit_{i}",
            "civilization": random.choice(civilizations),
            "attack": random.randrange(4, 12),
            "melee_armour": random.randrange(0, 6),
            "pierce_armour": random.randrange(0, 6),
            "hitpoints": random.randrange(40, 125),
            "bonus_attack": {},
            "attack_speed": random.randrange(75, 150) / 100,
            "type": random.choice(types),
            "unique": bool(random.getrandbits(1)),
            "cost": {},
            "image_url": ""
        }

        for j in range (0, 7):
            unit_number = random.randrange(1, 10)
            attack_bonus = random.randrange(1, 12)

            if unit_dict["name"] == f"unit_{unit_number}":
                pass
            else:
                unit_dict["bonus_attack"][f"unit_{unit_number}"] = attack_bonus

        unit_dict["cost"]["food"] = random.randrange(20, 100)
        unit_dict["cost"]["wood"] = random.randrange(20, 100)
        unit_dict["cost"]["gold"] = random.randrange(15, 65)



        units[f'''unit_{i}'''] = unit_dict

    f = open("testdb.py", "w")
    f.write(str(units))
    f.close()

    return units  


def counter_unit(unit_name, unit_data, technology_data):
    '''Function that calculates what unit counters what unit. The function is fed a unit_name and a dictionary
    with all the units present in the game, together with what techs are active (based on user input). 
    The function takes the initial attack value of a countering unit and adds to it any bonuses or armour class
    bonuses. It then sorts them and returns an array of 3-length tuples (unit name, counters, costs)  '''
    counter_object = []
    resources_cost = 0

    # Making sure we do not compare a unit against itself #
    for unit in unit_data.items():
        if str(unit_name) == str(unit[0]):
            continue

    # Strictly the unit object, with all the required information #
        unit_object = unit[1]
        unit_bonuses_tuple = unit_object["bonus_attack"].items()

        # Cost of recruiting one unit, adjusted to the difficulty of 
        # obtaining a resource

        resources_cost = ((unit_object["cost"]["food"] * 0.85) + (unit_object["cost"]["wood"] * 1) + (unit_object["cost"]["gold"] * 1.15))

        counter_value = unit_object["attack"]
        for element in unit_bonuses_tuple:
                if element[0] == unit_name:
                    counter_value += element[1]
       
        # Adding armour and attack types into the counter value
        counter_value -= unit_data[unit_name][f"{unit_object['type']}_armour"]

        # The damage a unit will cause is always at least 1. However, if the attack speed is smaller #
        # the unit will cause less than 1 damage per second 
        if counter_value == 0:  
            counter_value = 1

        counter_object.append((f"{unit_object['name']}", (counter_value * unit_object["attack_speed"]), (resources_cost)))
    
    return(sorted(counter_object, key = lambda x: x[1], reverse=True))

print(counter_unit("unit_1", create_units(), None))

