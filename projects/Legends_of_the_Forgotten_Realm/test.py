from player import Player
from enemy import get_random_enemy
from combat import battle
from armor import Armor
# # ==============================
# # TEST 1: CREATE PLAYER
# # ==============================

# player = Player("Jishnu", "Warrior")

# print("\n===== PLAYER CREATED =====")
# player.display_stats()


# # ==============================
# # TEST 2: CREATE RANDOM ENEMY
# # ==============================

# enemy = get_random_enemy(player.level)

# print("\n===== ENEMY CREATED =====")
# print(f"Enemy       : {enemy.name}")
# print(f"Level       : {enemy.level}")
# print(f"HP          : {enemy.hp}/{enemy.max_hp}")
# print(f"Attack      : {enemy.attack}")
# print(f"Defense     : {enemy.defense}")
# print(f"XP Reward   : {enemy.experience_reward}")
# print(f"Gold Reward : {enemy.gold_reward}")


# # ==============================
# # TEST 3: BATTLE
# # ==============================

# print("\n===== STARTING BATTLE =====")

# battle(player, enemy)


# # ==============================
# # TEST 4: FINAL PLAYER STATE
# # ==============================

# print("\n===== FINAL PLAYER STATE =====")

# player.display_stats()

# from armor import Armor

# armor = Armor("Steel Armor")

# print(armor.armor_name)
# print(armor.rarity)
# print(armor.defense)
# print(armor.hp_bonus)
# print(armor.mana_bonus)
# print(armor.crit_resistance)

# from armor import Armor

# armor = Armor("Steel Armor")

# print(armor.armor_name)
# print(armor.rarity)
# print(armor.defense)
# print(armor.hp_bonus)
# print(armor.mana_bonus)
# print(armor.crit_resistance)


from player import Player
from armor import Armor

player = Player("Jishnu", "Warrior")

armor = Armor("Steel Armor")
player.equip_armor(armor)

print(player.armor.armor_name)
print(player.armor.defense)
