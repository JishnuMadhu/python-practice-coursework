
from player import Player


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
    print('Character created!!!')

    return player

while True:

    player = create_player()
    player.display_stats()
    