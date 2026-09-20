from player import Player
from enemy import Enemy


def player_attack(player, enemy):

    damage = player.attack - enemy.defense

    if damage > 0:
        enemy.hp -= damage
        print(f'{player.name} dealt {damage} damage to {enemy.name}!')
        print(f'{enemy.name} has {enemy.hp}/{enemy.max_hp} HP remaining')

    else:
        damage = 0
        print(f"{enemy.name}'s defense is too high! No damage dealt.")


def enemy_attack(enemy, player):
    damage = enemy.attack - player.defense

    if damage > 0:
        player.hp -= damage
        print(f'{enemy.name} dealt {damage} damage to {player.name}!')
        print(f'{player.name} has {player.hp}/{player.max_hp} HP remaining')

    else:
        print(f"{player.name}'s defense is too high! No damage dealt.")

def battle(player, enemy):

    while player.hp > 0 and enemy.hp > 0:

        print('\n======================')
        print('       BATTLE       ')
        print('======================')
        print(f'{player.name} VS {enemy.name}')
        print(f'{player.name} HP: {player.hp}/{player.max_hp}')
        print(f'{enemy.name} HP: {enemy.hp}/{enemy.max_hp}')

        print('\nChoose your action')
        print('1. Attack')
        print('2. Run')

        choice = input('Enter your choice: ')

        if choice == '1':
            player_attack(player, enemy)

            if enemy.hp > 0:
                enemy_attack(enemy, player)

        elif choice == '2':
            print('You ran away!')
            break

        else:
            print('Invalid choice!')
    
        if enemy.hp <= 0:
            print(f'You defeated {enemy.name}!')
            print(f'{player.name} earned {enemy.experience_reward} experience points.')
            print(f'{player.name} earned {enemy.gold_reward} gold coins.')

            player.experience += enemy.experience_reward
            player.gold += enemy.gold_reward

            #player.check_level_up()
        
        elif player.hp <= 0:
            print(f'You were defeated by {enemy.name}!')
            print('GAME OVER')
            break   
        
# #test
# player = Player('jishnu','Mage')
# enemy = Enemy('Goblin',25)
# #player_attack(player,enemy)
# #enemy_attack(enemy,player)
# battle(player,enemy)