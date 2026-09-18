#Player Class

CLASS_STATS = {
        "Warrior": {
            "max_hp": 150,
            "max_mana": 50,
            "attack": 30,
            "defense": 25,
            "critical_chance": 10
        },

        "Mage": {
            "max_hp": 100,
            "max_mana": 150,
            "attack": 35,
            "defense": 10,
            "critical_chance": 15
        },

        "Archer": {
            "max_hp": 110,
            "max_mana": 100,
            "attack": 25,
            "defense": 15,
            "critical_chance": 25
        },

        "Assassin": {
            "max_hp": 80,
            "max_mana": 100,
            "attack": 35,
            "defense": 8,
            "critical_chance": 35
        }
}
class Player:

    def __init__(self, name,player_class):
        self.name = name
        self.player_class = player_class
        self.level = 1
        self.experience = 0

        self.stats = CLASS_STATS[player_class]  # assigning stats variable with selected player class from class stats dictionary

        self.hp = self.stats["max_hp"]
        self.max_hp = self.stats["max_hp"]

        self.mana = self.stats["max_mana"]
        self.max_mana = self.stats["max_mana"]

        self.attack = self.stats["attack"]
        self.defense = self.stats["defense"]
        

        self.gold = 0

        self.critical_chance = self.stats["critical_chance"]
        self.critical_damage = 2


    

    