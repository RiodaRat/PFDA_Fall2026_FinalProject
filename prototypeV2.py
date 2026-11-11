import random

#this is where I will be prototyping my code up until the final version

class Player: #player class and stats

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = 0


    def is_alive(self):
        return self.hp > 0

class Warrior(Player): #warrior class and stats and specific actions

    def __init__(self, name):
        super().__init__(name, hp=100, attack=20, defense=20)
        self.class_name = "Warrior"
        self.parry_chance = 0.30

    def parry(self):
        #potential to parry enemy attack and recieve no damage
        return random.random() < self.parry_chance
        

    def heal(self):
        #gives player a chance to heal themselves but leaves them open
        heal_amount = 30
        old_hp = self.hp

        self.hp = min(self.max_hp, self.hp + heal_amount)

        actual_healed = self.hp - old_hp

        print(f"You take a healing potion and recover {actual_healed} points of Health! your HP is now {self.hp}/{self.max_hp}. ")        

class Archer(Player): #archer class and stats with specific actions

    def __init__(self, name):
        super().__init__(name, hp=80, attack=30, defense=10)
        self.class_name = "Archer"
        self.dodge_chance = 0.30
        self.crit_chance = 0.30

    def try_dodge(self):
        return random.random() < self.dodge_chance

    def critcal_strike(self, enemy):
        num = random.random()
        if self.crit_chance > num:
            crit_damage = 60
            enemy.hp -= crit_damage
            print(f"You Steady your bow, fire . . . And get a CRITICAL HIT!! the {enemy.name} was dealt {crit_damage} points of damage! ")

        else:
            print("Your Attack misses and you are left open. ")

class Wizard(Player): #wizard class and stats with specific actions

    def __init__(self, name):
        super().__init__(name, hp=60, attack=10, defense=10)
        self.class_name = "Wizard"
        self.mana = 100

    def cast_mana_blast(self, enemy):
        #consume mana to deal heavy damage to enemy
        if self.mana >= 10:
            self.mana -= 10
            magic_damage = 40
            enemy.hp -= magic_damage
            print(f"You Channel arcane energy to deal a magic blast! the {enemy.name} was dealt {magic_damage} points of magic damage! You have {self.mana} Points of Mana left. ")
            return True
        else:
            print("You are out of Mana, the attack does nothing. ")
            return False

    def refill_mana(self):
        #refills mana gauge but leaves you open
        self.mana += 10
        print(f"You channel arcane energy to refill your Mana. You now have {self.mana} Points of Mana. ")

class Barbarian(Player): #barbarian class and stats with specific actions

    def __init__(self, name):
        super().__init__(name, hp=140, attack=30, defense=0)
        self.class_name = "Barbarian"
        self.raging = False

    def enter_rage(self):
        #boost attack power temporarily
        if not self.raging:
            self.raging = True
            self.attack += 20
            print(f"You Fly into a blinding RAGE! Your attack power surges!")
        else:
            print("You are already in a rage")

    def reset_rage(self):
        if self.raging:
            self.attack -= 20
            self.raging = False
            print("The rage subsides and you return to normal. ")

class Goblin: #monster class and stats

    def __init__(self):
        self.name = "Goblin"
        self.hp = 35
        self.attack = 12
        self.defense = 2

    def is_alive(self):
        return self.hp > 0

def invalid(): #function for when an option is invalid
    print("INVALID OPTION!! ")
    return

def choose_class(hero_name): #choosing heros class

    print("\nChoose Your Hero's Class:")
    print("1. Warrior / 2. Archer / 3. Wizard / 4. Barbarian")
    
    while True:
        choice = input("Enter choice (1-4): ")
        if choice == '1':
            return Warrior(hero_name)
        elif choice == '2':
            return Archer(hero_name)
        elif choice == '3':
            return Wizard(hero_name)
        elif choice == '4':
            return Barbarian(hero_name)
        else:
            invalid()


def run_combat(player, enemy): #combat loop

    #changing my combat loop out of the play game function and into its own seperate function

    print(f"\nA wild {enemy.name} blocks your path! ")

    while enemy.is_alive() and player.is_alive():
        print("----------------------------------------------------------")
        print(f"   COMBAT!! {player.name} (HP: {player.hp}/{player.max_hp}) VS {enemy.name} (HP: {enemy.hp}/{enemy.max_hp})   ")
        print("----------------------------------------------------------")
        
        print("\n ACTIONS: [1] to ATTACK, [2] to DEFEND, [3] to SPECIAL, [4] to SURRENDER ")
        action = input("CHOOSE YOUR ACTION!! ")

        if action == '1':
            damage = max(1, player.attack - enemy.defense)
            enemy.hp -= damage
            print(f"\nYou strike the {enemy.name} for {damage} Points of Physical Damage! The {enemy.name} has {enemy.hp}/{enemy.max_hp} HP left. ")

        elif action == '2':
            player.defense += 10
            print(f"\nYou brace for the enemies attack. ")

        elif action == '3':
            if player.class_name == "Warrior":
                print("\n Your SPECIAL actions include. [1] to PARRY and [2] to HEAL. ")
                war_action = input("CHOOSE YOUR ACTION!! or press [3] to back out. ")
                if war_action == '1':
                    player.parry()
                elif war_action == '2':
                    player.heal()
                elif war_action == '3':
                    continue
                else:
                    invalid()

            elif player.class_name == "Archer":
                print("\n Your SPECIAL actions include. [1] to DODGE and [2] to CRITICAL STRIKE. ")
                arch_action = input("CHOOSE YOUR ACTION!! or press [3] to back out. ")
                if arch_action == '1':
                    player.try_dodge()
                elif arch_action == '2':
                    player.critical_strike()
                elif arch_action == '3':
                    continue
                else:
                    invalid()

            elif player.class_name == "Wizard":
                print("\n Your SPECIAL actions include. [1] to MANA BLAST and [2] to REFILL. ")
                wiz_action = input("CHOOSE YOUR ACTION!! or press [3] to back out. ")
                if wiz_action == '1':
                    player.cast_mana_blast()
                elif wiz_action == '2':
                    player.refill_mana()
                elif wiz_action == '3':
                    continue
                else:
                    invalid()

            elif player.class_name == "Barbarian":
                print("\n Your SPECIAL actions include. [1] to RAGE. ")
                bar_action = input("CHOOSE YOUR ACTION!! or press [3] to back out. ")
                if bar_action == '1':
                    player.enter_rage()
                elif bar_action == '3':
                    continue
                else:
                    invalid()

        elif action == '4':
            sur_action = input("Are you sure you want to surrender??? [Y] for yes and [N] for no. ").lower()
            if sur_action == 'y':
                print(f"\nYou Surrender to {enemy.name} and become a slave to the dungeon and your run ends. ")
                player.hp = 0
                return False
            elif sur_action == 'n':
                print("You Clutch Your weapon tight and continue the fight! ")
                continue
            else:
                invalid()


def generate_random_events(): #function to generate random events 
    events = ["monster", "treasure", "empty"]
    return random.choice(events)


def play_game(): #main game loop
    print("=================================")
    print("  DUNGEON CRAWLER: PROTOTYPE V2  ")
    print("=================================")

    hero_name = input("What is your hero's name?: ")
    player = choose_class(hero_name)

    print(f"\nWelcome, {hero_name} the {player.class_name}! Your Journey begins as you step past the dungeon gates . . . ")

    #coordinate system for player position and dunegon map
    dungeon_map = {}
    player_pos = [0,0]

    #beginning safe point
    dungeon_map[tuple(player_pos)] = {"visited": True, "event": "start"}

    #main game loop
    while player.is_alive():
        print(f"\n-------------------------------------")
        print(f"Current Position: {player_pos} | HP: {player.hp}/{player.max_hp} | Gold: {player.gold}")
        print(f"-------------------------------------")
        #movement
        print("\n")
        move = input("Move [W: Up, S: Down, D: Right, A: Left] or [Q: Quit]: ").lower()

        if move == 'q':
            print("Retreating from the dungeon . . . See you next time!")
            break

        #calculate new position
        new_pos = list(player_pos)
        if move == 'w':
            new_pos[1] += 1
        elif move == 's':
            new_pos[1] -= 1
        elif move == 'd':
            new_pos[0] += 1
        elif move == 'a':
            new_pos[0] -= 1

        else:
            print("INVALID OPTION!! ")
            continue

        #update player position
        player_pos = new_pos
        coord_key = tuple(player_pos)

        #check if room has been visited before
        if coord_key not in dungeon_map:
            event = generate_random_events()
            dungeon_map[coord_key] = {"visited": True, "event": event}

            print(f"\n[Exploring new territory at {player_pos}]")

            if event == "monster":
                print(f"\nA wild Goblin Jumps out at you and challenges you to a fight!")
                enemy = Goblin()

                #combat loop
                while enemy.is_alive() and player.is_alive():
                    action = input("Combat actions --> [A] to attack or [R] to run: ").lower()

                    if action == 'a': #player attacks enemy 
                        

                        if enemy.is_alive(): #enemy counter attacks if still alive
                            damage_to_player = max(1, enemy.attack - player.defense)
                            player.hp -= damage_to_player
                            print(f"\nThe Goblin slashes back for {damage_to_player} damage! Your HP is now: {max(0, player.hp)})")

                    elif action == 'r':
                        print("\nYou managed to scramble away from the fight!")
                        break

                    else:
                        print("INVALID OPTION!! ")

                if not enemy.is_alive():
                    print("\nVictory! You defeated the Goblin and looted 20 gold. ")
                    player.gold += 20

            elif event == "treasure":
                print("\nYou stumble upon a treasure chest and gain 30 gold. ")
                player.gold += 30

            else:
                print("\nThe room is Quiet and empty, perfect place to catch your breath. ")

        else:
            print(f"\nYou step into a familiar room you have been in already. ")

    #end game check
    if not player.is_alive():
        print("\nGAME OVER! You died in the dungeon . . . ")

    else:
        print(f"\nThe Game closed and you finished with {player.gold} gold. ")

if __name__ == "__main__":
    play_game()


