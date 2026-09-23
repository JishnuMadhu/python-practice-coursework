



WEAPON_DATA = {

    "Rusty Sword": {
        "rarity": "Common",
        "damage": 5,
        "price": 20,
        "required_level": 1
    },

    "Iron Sword": {
        "rarity": "Uncommon",
        "damage": 10,
        "price": 50,
        "required_level": 2
    },

    "Steel Sword": {
        "rarity": "Rare",
        "damage": 15,
        "price": 100,
        "required_level": 5
    },

    "Flame Blade": {
        "rarity": "Epic",
        "damage": 25,
        "price": 250,
        "required_level": 10
    },

    "Demon Slayer": {
        "rarity": "Legendary",
        "damage": 40,
        "price": 500,
        "required_level": 20
    }
}

RARITY_DATA = {
    "Common": {
        "damage_multiplier": 1.0,
        "crit_bonus": 0
    },
    "Uncommon": {
        "damage_multiplier": 1.1,
        "crit_bonus": 2
    },
    "Rare": {
        "damage_multiplier": 1.3,
        "crit_bonus": 5
    },
    "Super Rare": {
        "damage_multiplier": 1.5,
        "crit_bonus": 8
    },
    "Epic": {
        "damage_multiplier": 1.8,
        "crit_bonus": 12
    },
    "Mythical": {
        "damage_multiplier": 2.2,
        "crit_bonus": 18
    },
    "Legendary": {
        "damage_multiplier": 2.8,
        "crit_bonus": 25
    }
}



class Weapon:

    def __init__(self, weapon_name):

        self.weapon_name = weapon_name

        data = WEAPON_DATA[weapon_name]

        self.rarity = data["rarity"]
        self.base_damage = data["damage"]
        self.price = data["price"]
        self.required_level = data["required_level"]

        rarity_data = RARITY_DATA[self.rarity]

        self.damage_multiplier = rarity_data["damage_multiplier"]
        self.crit_bonus = rarity_data["crit_bonus"]

        self.damage = int(self.base_damage * self.damage_multiplier)

#test 
# weapon = Weapon("Rusty Sword")
# print(weapon.weapon_name)
# print(weapon.rarity)
# print(weapon.damage)
# print(weapon.crit_bonus)
# print(weapon.price)
# print(weapon.required_level)
# print(weapon.rarity)
