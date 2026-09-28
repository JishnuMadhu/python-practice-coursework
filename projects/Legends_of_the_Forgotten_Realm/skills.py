SKILLS = {
    "Warrior": {
        "Slash": {
            "mana_cost": 0,
            "damage": 20
        },
        "Shield Bash": {
            "mana_cost": 10,
            "damage": 15
        },
        "Rage": {
            "mana_cost": 15,
            "damage": 25
        },
        "Earthquake": {
            "mana_cost": 30,
            "damage": 40
        }
    },

    "Mage": {
        "Fireball": {
            "mana_cost": 10,
            "damage": 25
        },
        "Ice Blast": {
            "mana_cost": 15,
            "damage": 30
        },
        "Thunder Strike": {
            "mana_cost": 25,
            "damage": 45
        },
        "Meteor": {
            "mana_cost": 40,
            "damage": 60
        }
    },

    "Archer": {
        "Multi Shot": {
            "mana_cost": 10,
            "damage": 25
        },
        "Poison Arrow": {
            "mana_cost": 15,
            "damage": 30
        },
        "Explosive Arrow": {
            "mana_cost": 25,
            "damage": 45
        },
        "Sniper Shot": {
            "mana_cost": 35,
            "damage": 60
        }
    },

    "Assassin": {
        "Backstab": {
            "mana_cost": 10,
            "damage": 30
        },
        "Smoke Bomb": {
            "mana_cost": 15,
            "damage": 20
        },
        "Shadow Strike": {
            "mana_cost": 25,
            "damage": 45
        },
        "Instant Kill": {
            "mana_cost": 50,
            "damage": 80
        }
    }
}


def use_skill(player, enemy):

    class_skills = SKILLS[player.character_class]

    print("\n===== SKILLS =====")

    skill_names = list(class_skills.keys())

    for i, skill_name in enumerate(skill_names, start=1):
        skill = class_skills[skill_name]
        print(f"{i}. {skill_name} | Mana: {skill['mana_cost']} | Damage: {skill['damage']}")

    try:
        choice = int(input("Choose a skill: "))

        if choice < 1 or choice > len(skill_names):
            print("Invalid choice!")
            return False

        skill_name = skill_names[choice - 1]
        skill = class_skills[skill_name]

        if player.mana < skill["mana_cost"]:
            print("Not enough mana!")
            return False

        player.mana -= skill["mana_cost"]

        damage = player.attack + skill["damage"] - enemy.defense

        if damage < 0:
            damage = 0

        enemy.hp -= damage

        if enemy.hp < 0:
            enemy.hp = 0

        print(f"\nUsed {skill_name}!")
        print(f"Damage dealt: {damage}")
        print(f"Enemy HP: {enemy.hp}/{enemy.max_hp}")
        print(f"Mana remaining: {player.mana}/{player.max_mana}")
        return True

    except ValueError:
        print("Please enter a number!")
        return False
