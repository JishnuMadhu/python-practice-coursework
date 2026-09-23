
from enemy import get_random_enemy
from player import Player
from combat import battle
from weapons import Weapon

def create_player():
    classes = {
        1: "Warrior",
        2: "Mage",
        3: "Archer",
        4: "Assassin"
    }
    while True:
        name = input("Enter name:-")

        if name.strip():
            break

        print("Name cannot be empty!")

    while True:
        try:
            ch = int(input(f'Choose your class\n1. Warrior\n2. Mage\n3. Archer\n4. Assassin:-'))

            if ch in classes:
                player_class = classes[ch]
                break
            else:
                print('Invalid choice')

        except ValueError:
            print('Plese enter a number!!!')
    

    player = Player(name,player_class)
    print('===== PLAYER CREATED =====')

    return player




player = Player("jishnu", "Warrior")

weapon = Weapon("Rusty Sword")
player.equip_weapon(weapon)

enemy = get_random_enemy(player.level)

battle(player, enemy)
        # player = Player('jishnu', "Warrior")
        # player.level = 2
        # player.defense = 5
        # player.critical_chance = 100

        # enemy = get_random_enemy(player.level)
        # battle(player, enemy)
        # player.display_stats()