
from player import Player

while True:
    name = input('enter name:-')
    ch = input(f'Choose your class\n1. Warrior\n2. Mage\n3. Archer\n4. Assassin')
    if ch == 1:
        player_class = 'Warrior'
    elif ch == 2:
        player_class = 'Mage'
    elif ch == 3:
        player_class = 'Archer'
    elif ch == 4:
        player_class = 'Assassin'
    else:
        print("Invalid choice!!!")

    player = Player(name,player_class)
    print(player.name)
    print(player.player_class)
    print(player.hp)
    print(player.max_hp)
    print(player.mana)
    print(player.attack)
    print(player.defense)
    print(player.critical_chance)