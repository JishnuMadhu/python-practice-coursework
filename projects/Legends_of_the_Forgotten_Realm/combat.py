from player import Player
from enemy import Enemy
from weapons import Weapon
import random
from enemy import get_random_enemy


def player_attack(player, enemy):
    if player.weapon is None:
        weapon_damage = 0
    else:
        weapon_damage = player.weapon.damage
    damage = player.attack + weapon_damage - enemy.defense

    if damage > 0:

        if random.randint(1,100) <= player.critical_chance:
            damage = damage * player.critical_damage
            print("CRITICAL HIT!")

        enemy.hp = max(0,enemy.hp - damage)
        
        print(f'{player.name} dealt {damage} damage to {enemy.name}!')
        print(f'{enemy.name} has {enemy.hp}/{enemy.max_hp} HP remaining')

    else:
        damage = 0
        print(f"{enemy.name}'s defense is too high! No damage dealt.")


def enemy_attack(enemy, player):
    damage = enemy.attack - player.defense

    if damage > 0:

        if player.is_defending:
            damage = damage // 2
            print(f'{player.name} takes half damage!')
            
        player.hp = max(0, player.hp - damage)

        print(f'{enemy.name} dealt {damage} damage to {player.name}!')
        print(f'{player.name} has {player.hp}/{player.max_hp} HP remaining')
        
    else:
        print(f"{player.name}'s defense is too high! No damage dealt.")
    
    player.is_defending = False   # after enemy attack, reset defense

def player_defend(player):
    player.is_defending = True
    print(f'{player.name} is defending...')

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
        print('2. Defend')
        print('3. Run')

        choice = input('Enter your choice: ')

        if choice == '1':
            player_attack(player, enemy)

            if enemy.hp > 0:
                enemy_attack(enemy, player)
                
        elif choice == '2':
            player_defend(player)

            if enemy.hp > 0:
                enemy_attack(enemy,player)

        elif choice == '3':
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

            player.check_level_up()
        
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

# player = Player("jishnu", "Warrior")

# weapon = Weapon("Rusty Sword")
# player.equip_weapon(weapon)

# enemy = get_random_enemy(player.level)

# battle(player, enemy)

