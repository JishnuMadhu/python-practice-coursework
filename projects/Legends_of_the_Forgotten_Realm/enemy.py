import random


ENEMY_DATA = {

    #  LEVEL 1–10
    "Goblin": {
        "hp": 40,
        "attack": 10,
        "defense": 5,
        "experience": 20,
        "gold": 10
    },

    "Wolf": {
        "hp": 35,
        "attack": 15,
        "defense": 3,
        "experience": 25,
        "gold": 12
    },

    "Slime": {
        "hp": 50,
        "attack": 8,
        "defense": 8,
        "experience": 20,
        "gold": 8
    },

    "Zombie": {
        "hp": 60,
        "attack": 12,
        "defense": 10,
        "experience": 30,
        "gold": 15
    },

    "Skeleton": {
        "hp": 45,
        "attack": 14,
        "defense": 7,
        "experience": 28,
        "gold": 13
    },


    # LEVEL 11–20

    "Orc": {
        "hp": 90,
        "attack": 22,
        "defense": 15,
        "experience": 50,
        "gold": 25
    },

    "Bandit": {
        "hp": 75,
        "attack": 25,
        "defense": 10,
        "experience": 45,
        "gold": 30
    },

    "Troll": {
        "hp": 120,
        "attack": 20,
        "defense": 20,
        "experience": 60,
        "gold": 28
    },

    "Dark Archer": {
        "hp": 70,
        "attack": 28,
        "defense": 8,
        "experience": 55,
        "gold": 32
    },

    "Giant Spider": {
        "hp": 85,
        "attack": 24,
        "defense": 12,
        "experience": 52,
        "gold": 27
    },


    # LEVEL 21–30 

    "Vampire": {
        "hp": 150,
        "attack": 32,
        "defense": 18,
        "experience": 80,
        "gold": 45
    },

    "Werewolf": {
        "hp": 140,
        "attack": 38,
        "defense": 15,
        "experience": 85,
        "gold": 50
    },

    "Necromancer": {
        "hp": 110,
        "attack": 40,
        "defense": 12,
        "experience": 90,
        "gold": 55
    },

    "Ice Golem": {
        "hp": 200,
        "attack": 30,
        "defense": 30,
        "experience": 100,
        "gold": 60
    },

    "Fire Demon": {
        "hp": 170,
        "attack": 42,
        "defense": 20,
        "experience": 110,
        "gold": 65
    }
}

ENEMY_RANGES = {
    (1, 10): [
        "Goblin",
        "Wolf",
        "Slime",
        "Zombie",
        "Skeleton"
    ],

    (11, 20): [
        "Orc",
        "Bandit",
        "Troll",
        "Dark Archer",
        "Giant Spider"
    ],

    (21, 30): [
        "Vampire",
        "Werewolf",
        "Necromancer",
        "Ice Golem",
        "Fire Demon"
    ]
}


def get_random_enemy(player_level):
    for level_range,enemies in ENEMY_RANGES.items():
        min_level,max_level = level_range
        if min_level <= player_level <= max_level:
            enemy_name = random.choice(enemies)
            return enemy_name
            # return Enemy(enemy_name,player_level)


#test 
print(get_random_enemy(9))
class Enemy:

    def __init__(self, name, level):

        self.name = name
        self.level = level

        self.enemy_stats = ENEMY_DATA[name]

        self.level_scaling = 1 + (level - 1) * 0.10  #factor with which enemy stats increases by level by 10%


        self.hp = int(self.enemy_stats["hp"] * self.level_scaling)
        self.max_hp = self.hp

        self.attack = int(self.enemy_stats["attack"] * self.level_scaling)
        self.defense = int(self.enemy_stats["defense"] * self.level_scaling)

        reward_scaling = 1 + (level - 1) * 0.05  #factor with which enemy rewards increases by level by 5%

        self.experience_reward = int(self.enemy_stats['experience'] * reward_scaling)
        self.gold_reward = int(self.enemy_stats['gold'] * reward_scaling)


#test
# enemy = Enemy("Goblin", 99)

# print(enemy.name)
# print(enemy.level)
# print(enemy.hp)
# print(enemy.max_hp)
# print(enemy.attack)
# print(enemy.defense)
# print(enemy.experience_reward)
# print(enemy.gold_reward)

# print(ENEMY_DATA['Orc'])
# print()
# print(ENEMY_RANGES[(21,30)])


