import random

class Player: #player class and stats

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 25
        self.defense = 5
        self.gold = 0


    def is_alive(self):
        return self.hp > 0


class Goblin: #monster class and stats

    def __init__(self):
        self.name = "Goblin"
        self.hp = 35
        self.attack = 12
        self.defense = 2

    def is_alive(self):
        return self.hp > 0


def generate_random_events(): #function to generate random events 
    events = ["monster", "treasure", "empty"]
    return random.choice(events)

def play_game(): #function to play the game
    print("=================================")
    print("  DUNGEON CRAWLER: PROTOTYPE V1  ")
    print("=================================")

    hero_name = input("What is your hero's name?: ")
    player = Player(hero_name)

    #coordinate system for player position and dunegon map
    dungeon_map = {}
    player_pos = [0,0]

    #beginning safe point
    dungeon_map[tuple(player_pos)] = {"visited": True, "event": "start"}
    print(f"\nWelcome {player.name}! Your Journey begins as you step past the dungeon gates . . . ")

    #main game loop
    while player.is_alive(True):
        print(f"\n-------------------------------------")
        print(f"Current Position: {player.pos} | HP: {player.hp}/{player.max_hp} | Gold: {player.gold}")

        #movement
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
                print(f"\n A wild Goblin Jumps out at you and challenges you to a fight!")
                enemy = Goblin()

                #combat loop
                while enemy.is_alive(True) and player.is_alive(True):
                    action = input("Combat actions --> [A] to attack or [R] to run: ").lower()

                    if action == 'a': #player attacks enemy 
                        damage_to_enemy = max(1, player.attack - enemy.defense)
                        enemy.hp -= damage_to_enemy
                        print(f" You strike the Goblin for {damage_to_enemy} damage! The Goblin has ({max(0, enemy.hp)} HP left)")

                        if enemy.is_alive(True): #enemy counter attacks if still alive
                            damage_to_player = max(1, enemy.attack - player.defense)
                            player.hp -= damage_to_player
                            print(f" The Goblin slashes back for {damage_to_player} damage! Your HP is now: {max(0, player.hp)})")

                    elif action == 'r':
                        print("You managed to scramble away from the fight!")
                        break

                    else:
                        print("INVALID OPTION!! ")

                if enemy.is_alive(False):
                    print("\n Victory! You defeated the Goblin and looted 20 gold. ")
                    player.gold += 20

            elif event == "treasure":
                print("you stumble upon a treasure chest and gain 30 gold. ")
                player.gold += 30

            else:
                print("The room is Quiet and empty, perfect place to catch your breath. ")

        else:
            print(f"\n You step into a familiar room you have been in already. ")

    #end game check
    if player.is_alive(False):
        print("\n GAME OVER! You died in the dungeon . . . ")

    else:
        print(f"\n the Game closed and you finished with {player.gold} gold. ")

if __name__ == "__main__":
    play_game()


