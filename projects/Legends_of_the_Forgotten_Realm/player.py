#Player Class
from weapons import Weapon


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
        self.character_class = player_class
        self.level = 1
        self.experience = 0

        self.stats = CLASS_STATS[player_class]  # assigning stats variable with selected player class from class stats dictionary

        self.hp = self.stats["max_hp"]
        self.max_hp = self.stats["max_hp"]

        self.mana = self.stats["max_mana"]
        self.max_mana = self.stats["max_mana"]

        self.attack = self.stats["attack"]
        self.defense = self.stats["defense"]
        
        self.is_defending = False #to know whether the player is defending or not
        
        self.gold = 0
        self.weapon = None

        self.base_critical_chance = self.stats["critical_chance"]
        self.critical_chance = self.base_critical_chance

        self.critical_damage = 2

        self.armor = None

        self.critical_resistance = 0

        self.weapons = []
        self.armors = []
        self.potions = []

        self.bosses_defeated = []
        self.enemies_defeated = 0

    def display_stats(self):
        print('========================')
        print('     PLAYER STATS     ')
        print('========================')

        
        print(f'Name       : {self.name}')
        print(f'Class      : {self.player_class}')
        print(f'Level      : {self.level}')
        print(f'Experience : {self.experience}')
        print(f'HP         : {self.hp} / {self.max_hp}')
        print(f'Mana       : {self.mana} / {self.max_mana}')

        print(f'Attack     : {self.attack}')
        print(f'Defense    : {self.defense}')
        print(f'Crit Chance: {self.critical_chance}%')
        print(f'Gold       : {self.gold}')
    
    def check_level_up(self):
        while self.experience >= self.level * 100: # check if player has enough experience to level up

                required_xp = self.level * 100  #calculate required experience for next level

                self.experience -= required_xp
                self.level += 1

                self.max_hp += 10
                self.max_mana += 10
                self.attack += 5
                self.defense += 5
                self.critical_chance += 2

                self.hp = self.max_hp  #resets hp to max hp after level up
                self.mana = self.max_mana  #resets mana to max mana after level up

                print(f'You leveled up to {self.level}!')
                print('Your HP and Mana have been fully restored!')
    
    def equip_weapon(self, weapon):

        if self.level < weapon.required_level:
            print(
                f"You need to be level {weapon.required_level} "
                f"to equip {weapon.weapon_name}!"
            )
            return False

        self.weapon = weapon
        self.critical_chance = self.base_critical_chance + weapon.crit_bonus

        print(f"{weapon.weapon_name} equipped!")
        print(f"Damage: {weapon.damage}")
        print(f"Critical Chance: {self.critical_chance}%")

        return True   

    def equip_armor(self, armor):

        if self.level < armor.required_level:
            print(
                f"You need to be level {armor.required_level} "
                f"to equip {armor.armor_name}!"
            )
            return False

        if self.armor is not None:
            self.defense -= self.armor.defense
            self.max_hp -= self.armor.hp_bonus
            self.max_mana -= self.armor.mana_bonus
            self.critical_resistance -= self.armor.crit_resistance

        self.armor = armor

        self.defense += armor.defense
        self.max_hp += armor.hp_bonus
        self.max_mana += armor.mana_bonus
        self.critical_resistance += armor.crit_resistance

        self.hp = min(self.hp, self.max_hp)
        self.mana = min(self.mana, self.max_mana)

        print(f"{armor.armor_name} equipped!")
        print(f"Defense: {self.defense}")
        print(f"Max HP: {self.max_hp}")
        print(f"Max Mana: {self.max_mana}")
        print(f"Critical Resistance: {self.critical_resistance}%")

        return True

    def use_potion(self, potion):

        if potion.type == "health":

            if potion.value == "full":
                self.hp = self.max_hp
            else:
                self.hp = min(self.max_hp, self.hp + potion.value)

            print(f"Used {potion.potion_name}!")
            print(f"HP: {self.hp}/{self.max_hp}")

        elif potion.type == "mana":

            if potion.value == "full":
                self.mana = self.max_mana
            else:
                self.mana = min(self.max_mana, self.mana + potion.value)

            print(f"Used {potion.potion_name}!")
            print(f"Mana: {self.mana}/{self.max_mana}")

        elif potion.type == "mixed":

            if potion.value == "full":
                self.hp = self.max_hp
                self.mana = self.max_mana
            else:
                self.hp = min(self.max_hp, self.hp + potion.value)
                self.mana = min(self.max_mana, self.mana + potion.value)

            print(f"Used {potion.potion_name}!")
            print(f"HP: {self.hp}/{self.max_hp}")
            print(f"Mana: {self.mana}/{self.max_mana}")

        elif potion.type == "attack_buff":
            self.attack += potion.value
            print(f"Attack increased by {potion.value}!")

        elif potion.type == "defense_buff":
            self.defense += potion.value
            print(f"Defense increased by {potion.value}!")

        elif potion.type == "crit_buff":
            self.critical_chance += potion.value
            print(f"Critical Chance increased by {potion.value}%!")

    def add_potion(self, potion):
        self.potions.append(potion)
        print(f'{potion.potion_name} added to inventory!')

    def show_potions(self):

        if not self.potions:
            print("No potions in inventory.")
            return

        print("\n===== POTIONS =====")

        for i, potion in enumerate(self.potions, start=1):
            print(f"{i}. {potion.potion_name}")

    def use_potion_from_inventory(self):

        if not self.potions:
            print("You have no potions!")
            return

        self.show_potions()

        try:
            choice = int(input("Choose a potion: "))

            if choice < 1 or choice > len(self.potions):
                print("Invalid choice!")
                return

            potion = self.potions[choice - 1]

            self.use_potion(potion)

            self.potions.remove(potion)

        except ValueError:
            print("Please enter a number!")

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f"{weapon.weapon_name} added to inventory!")

    def show_weapons(self):
        if not self.weapons:
            print("No weapons in inventory.")
            return

        print("\n===== WEAPONS =====")

        for i, weapon in enumerate(self.weapons, start=1):
            print(
                f"{i}. {weapon.weapon_name} | "
                f"{weapon.rarity} | "
                f"Damage: {weapon.damage}"
            )

    def add_armor(self, armor):
        self.armors.append(armor)
        print(f"{armor.armor_name} added to inventory!")

    def show_armors(self):
        if not self.armors:
            print("No armor in inventory.")
            return

        print("\n===== ARMOR =====")

        for i, armor in enumerate(self.armors, start=1):
            print(
                f"{i}. {armor.armor_name} | "
                f"{armor.rarity} | "
                f"Defense: {armor.defense}"
            )

    def equip_weapon_from_inventory(self):
        if not self.weapons:
            print("No weapons in inventory to equip.")
            return

        self.show_weapons()
        try:
            choice = int(input("\nChoose a weapon to equip (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.weapons):
                print("Invalid choice!")
                return

            chosen_weapon = self.weapons[choice - 1]
            self.equip_weapon(chosen_weapon)
        except ValueError:
            print("Please enter a number!")

    def equip_armor_from_inventory(self):
        if not self.armors:
            print("No armor in inventory to equip.")
            return

        self.show_armors()
        try:
            choice = int(input("\nChoose armor to equip (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.armors):
                print("Invalid choice!")
                return

            chosen_armor = self.armors[choice - 1]
            self.equip_armor(chosen_armor)
        except ValueError:
            print("Please enter a number!")

    def inventory_menu(self):
        while True:
            print("\n========== INVENTORY ==========")
            eq_weapon = self.weapon.weapon_name if self.weapon else "None"
            eq_armor = self.armor.armor_name if self.armor else "None"
            print(f"Equipped Weapon: {eq_weapon}")
            print(f"Equipped Armor : {eq_armor}")
            print("-------------------------------")
            print("1. View Weapons")
            print("2. Equip Weapon")
            print("3. View Armor")
            print("4. Equip Armor")
            print("5. View Potions")
            print("6. Use Potion")
            print("7. Back")

            try:
                choice = int(input("\nChoose an option: "))
                if choice == 1:
                    self.show_weapons()
                elif choice == 2:
                    self.equip_weapon_from_inventory()
                elif choice == 3:
                    self.show_armors()
                elif choice == 4:
                    self.equip_armor_from_inventory()
                elif choice == 5:
                    self.show_potions()
                elif choice == 6:
                    self.use_potion_from_inventory()
                elif choice == 7:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")

# test
# player = Player("Jishnu", "Warrior")
# weapon = Weapon("Rusty Sword")
# player.equip_weapon(weapon)
# print(player.weapon.weapon_name)
# print(player.weapon.damage)
