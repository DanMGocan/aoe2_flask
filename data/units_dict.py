units = {

    # Longbowman #
    "longbowman" : {
        "elite": False,
        "name": "longbowman",
        "added_in": "the_age_of_kings",
        "description": "British unique archer with very long range.",
        "type": "foot_archer",
        "civilization": "britons", 
        "age": "castle_age",
        "trained_at": {
            "castle": 18
        },
        "cost": {
            "food": 0,
            "wood": 35,
            "gold": 40
        },
        "hit_points": 35,
        "pierce_attack": 6,
        "melee_attack": None,
        "attack_bonus": {
            "spearman": 2
        },
        "rate_of_fire": 2, # attacks once every X seconds
        "frame_delay": 10,
        "attack_delay": 0.5,
        "range": 5,
        "accuracy": 70/100,
        "projectile_speed": 7,
        "melee_armour": 0,
        "pierce_armour": 0,
        "armour_class": {
            "archer": 0,
            "unique_unit": 0
        },
        "speed": 0.96,
        "line_of_sight": 7
    },

    # Elite Longbowman #
    "elite_longbowman" : {
        "elite": True,
        "name": "elite_longbowman",
        "added_in": "the_age_of_kings",
        "description": "British unique archer with very long range.",
        "type": "foot_archer",
        "civilization": "britons", 
        "age": "imperial_age",
        "trained_at": {
            "castle": 18
        },
        "cost": {
            "food": 0,
            "wood": 35,
            "gold": 40
        },
        "hit_points": 40,
        "pierce_attack": 7,
        "melee_attack": None,
        "attack_bonus": {
            "spearman": 2
        },
        "rate_of_fire": 2, # attacks once every X seconds
        "frame_delay": 10,
        "attack_delay": 0.5,
        "range": 6,
        "accuracy": 80/100,
        "projectile_speed": 7,
        "melee_armour": 0,
        "pierce_armour": 1,
        "armour_class": {
            "archer": 0,
            "unique_unit": 0
        },
        "speed": 0.96,
        "line_of_sight": 8
    },

    # Cataphract #
    "cataphract" : {
        "elite": False,
        "name": "cataphract",
        "added_in": "the_age_of_kings",
        "description": "Byzantine unique cavalry unit.",
        "type": "cavalry",
        "civilization": "byzantines", 
        "age": "castle_age",
        "trained_at": {
            "castle": 20
        },
        "cost": {
            "food": 70,
            "wood": 0,
            "gold": 75
        },
        "hit_points": 110,
        "pierce_attack": None,
        "melee_attack": 9,
        "attack_bonus": {
            "infantry": 9,
            "condottiero": 9
        },
        "rate_of_fire": 1.8, # attacks once every X seconds
        "trample_damage_radius": None,
        "trample_damage": {
            "ignore_armour": None,
            "armour": None
        },
        "frame_delay": None,
        "attack_delay": None,
        "range": None,
        "accuracy": None,
        "projectile_speed": None,
        "melee_armour": 2,
        "pierce_armour": 1,
        "armour_class": {
            "cavalry": 12,
            "unique_unit": 0
        },
        "speed": 1.35,
        "line_of_sight": 4
    },

    # Elite Cataphract #
    "elite_cataphract" : {
        "elite": True,
        "name": "elite_cataphract",
        "added_in": "the_age_of_kings",
        "description": "Byzantine unique cavalry unit.",
        "type": "cavalry",
        "civilization": "byzantines", 
        "age": "imperial_age",
        "trained_at": {
            "castle": 20
        },
        "cost": {
            "food": 70,
            "wood": 0,
            "gold": 75
        },
        "hit_points": 150,
        "pierce_attack": None,
        "melee_attack": 12,
        "attack_bonus": {
            "infantry": 12,
            "condottiero": 10
        },
        "rate_of_fire": 1.7, # attacks once every X seconds
        "trample_damage_radius": 0.5,
        "trample_damage": {
            "ignore_armour": 5,
            "armour": None
        },
        "frame_delay": None,
        "attack_delay": None,
        "range": None,

        "accuracy": None,
        "projectile_speed": None,
        "melee_armour": 2,
        "pierce_armour": 1,
        "armour_class": {
            "cavalry": 16,
            "unique_unit": 0
        },
        "speed": 1.35,
        "line_of_sight": 5
    },

    # Woad Raider #
    "woad_raider" : {
        "elite": False,
        "name": "woad_raider",
        "added_in": "the_age_of_kings",
        "description": "Celtic unique infantry unit. Fast-moving.",
        "type": "infantry",
        "civilization": "celts", 
        "age": "castle_age",
        "trained_at": {
            "castle": 10
        },
        "cost": {
            "food": 65,
            "wood": 0,
            "gold": 25
        },
        "hit_points": 65,
        "pierce_attack": None,
        "melee_attack": 10,
        "attack_bonus": {
            "eagle_warrior": 2,
            "standard_building": 2
        },
        "rate_of_fire": 1.7, # attacks once every X seconds
        "trample_damage_radius": None,
        "trample_damage": {
            "ignore_armour": None,
            "armour": None
        },
        "frame_delay": None,
        "attack_delay": None,
        "range": None,
        "accuracy": None,
        "projectile_speed": None,
        "melee_armour": 2,
        "pierce_armour": 1,
        "armour_class": {
            "cavalry": 16,
            "unique_unit": 0
        },
        "speed": 1.35,
        "line_of_sight": 5
    },

    # Elite Woad Raider #
    "elite_woad_raider" : {
        "elite": True,
        "name": "elite_woad_raider",
        "added_in": "the_age_of_kings",
        "description": "Celtic unique infantry unit. Fast-moving.",
        "type": "infantry",
        "civilization": "celts", 
        "age": "imperial_age",
        "trained_at": {
            "castle": 10
        },
        "cost": {
            "food": 65,
            "wood": 0,
            "gold": 25
        },
        "hit_points": 80,
        "pierce_attack": None,
        "melee_attack": 13,
        "attack_bonus": {
            "eagle_warrior": 3,
            "standard_building": 3
        },
        "rate_of_fire": 2,
        "trample_damage_radius": None,
        "trample_damage": {
            "ignore_armour": None,
            "armour": None
        },
        "frame_delay": None,
        "attack_delay": None,
        "range": None,
        "accuracy": None,
        "projectile_speed": None,
        "melee_armor": 0,
        "pierce_armor": 1,
        "armor_class": {
            "infantry": 0,
            "unique_unit": 0
        },
        "speed": 1.38,
        "line_of_sight": 5
    },

    # Chu Ko Nu #
    "chu_ko_nu" : {
        "elite": False,
        "name": "chu_ko_nu",
        "added_in": "the_age_of_kings",
        "description": "Chinese unique archer with rapid-fire attack.",
        "type": "foot_archer",
        "civilization": "chinese", 
        "age": "castle_age",
        "trained_at": {
            "castle": 16
        },
        "cost": {
            "food": 0,
            "wood": 40,
            "gold": 35
        },
        "hit_points": 45,
        "pierce_attack": 8,
        "melee_attack": 0,
        "attack_bonus": {
            "spearman": 2
        },
        "rate_of_fire": 3.44,
        "trample_damage_radius": None,
        "trample_damage": {
            "ignore_armour": None,
            "armour": None
        },
        "frame_delay": 19,
        "attack_delay": 0.23,
        "range": 4,
        "accuracy": 85/100,
        "projectile_speed": 7,
        "melee_armor": 0,
        "pierce_armor": 0,
        "armor_class": {
            "archer": 0,
            "unique_unit": 0
        },
        "speed": 0.96,
        "line_of_sight": 6
    },

    # Elite Chu Ko Nu #
    "elite_chu_ko_nu" : {
        "elite": True,
        "name": "chu_ko_nu",
        "added_in": "the_age_of_kings",
        "description": "Chinese unique archer with rapid-fire attack.",
        "type": "foot_archer",
        "civilization": "chinese", 
        "age": "castle_age",
        "trained_at": {
            "castle": 13
        },
        "cost": {
            "food": 0,
            "wood": 40,
            "gold": 35
        },
        "hit_points": 50,
        "pierce_attack": 8,
        "melee_attack": 0,
        "attack_bonus": {
            "spearman": 2
        },
        "rate_of_fire": 3.89,
        "trample_damage_radius": None,
        "trample_damage": {
            "ignore_armour": None,
            "armour": None
        },
        "frame_delay": 19,
        "attack_delay": 0.23,
        "range": 4,
        "accuracy": 85/100,
        "projectile_speed": 7,
        "melee_armor": 0,
        "pierce_armor": 0,
        "armor_class": {
            "archer": 0,
            "unique_unit": 0
        },
        "speed": 0.96,
        "line_of_sight": 6
    },

     # Throwing Axeman #
    "throwing_axeman" : {
        "elite": False,
        "name": "throwing_axeman",
        "added_in": "the_age_of_kings",
        "description": "Frankish unique infantry unit with ranged melee attack.",
        "type": "foot_archer",
        "civilization": "chinese", 
        "age": "castle_age",
        "trained_at": {
            "castle": 13
        },
        "cost": {
            "food": 0,
            "wood": 40,
            "gold": 35
        },
        "hit_points": 50,
        "pierce_attack": 8,
        "melee_attack": 0,
        "attack_bonus": {
            "spearman": 2
        },
        "rate_of_fire": 3.89,
        "trample_damage_radius": None,
        "trample_damage": {
            "ignore_armour": None,
            "armour": None
        },
        "frame_delay": 19,
        "attack_delay": 0.23,
        "range": 4,
        "accuracy": 85/100,
        "projectile_speed": 7,
        "melee_armor": 0,
        "pierce_armor": 0,
        "armor_class": {
            "archer": 0,
            "unique_unit": 0
        },
        "speed": 0.96,
        "line_of_sight": 6
    },
}
    





