# DTS assignment ----- 24/3/26 ----- Cameron Christie

# ----------------------- Library -----------------------
import time
import random
import copy

# ----------------------- Variables -----------------------

# Dictionaries and lists
player_stats = {}

player_equipment = {
    "Weapon": {},

    "Armour": {
        "Name": "Wooden Armour",
        "Weakness": ["None"],
        "Strong against": ["None"]}
}

item_inventory = []

DAMAGE_VALUES = {"Normal": 1, "Strong": 2, "Weak": 0.5}

POSSIBLE_CLASSES = [
    {"Name": "Knight",
     "Stats": {"Health": 20, "Bonus damage": 5, "Defense": 2, "Strength": 1, "Stamina": 8}},
    {"Name": "Wizard",
     "Stats": {"Health": 15, "Bonus damage": 10, "Defense": 1, "Strength": 0.5, "Stamina": 20}},
    {"Name": "Warrior",
     "Stats": {"Health": 30, "Bonus damage": 0, "Defense": 1, "Strength": 3, "Stamina": 10}}
]

POSSIBLE_WEAPONS = {
    "tutorial": [
        {"Name": "Starter Sword",
            "Info": [
                {"Move name": "Stab", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Slash", "Base damage": 3, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Jab", "Base damage": 4, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2}]},
        {"Name": "Starter Wand",
            "Info": [
                {"Move name": "Zap", "Base damage": 6, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Fireball", "Base damage": 5, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3},
                {"Move name": "Poke", "Base damage": 2, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1}]},
        {"Name": "Starter Axe",
            "Info": [
                {"Move name": "Cut", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Throw axe", "Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2}]}
    ],
    "Shop 1": [
        {"Name": "Sword",
            "Info": [
                {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Move 2", "Base damage": 2, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Move 3", "Base damage": 7, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
            ]},
        {"Name": "Bow",
            "Info": [
                {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 1},
                {"Move name": "Move 2", "Base damage": 2, "Hit multi enemy": True, "Type": "Ranged", "Stamina use": 2},
                {"Move name": "Move 3", "Base damage": 7, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3}]}
    ]
}

POSSIBLE_ARMOUR = [
    {
        "Name": "Chainmail",
        "Weakness": ["Magic"],
        "Strong against": ["Melee","Ranged"]
    },
    {
        "Name": "Knights Armour",
        "Weakness": ["Magic"],
        "Strong against": ["Melee","Ranged"]
    }
]

POSSIBLE_ENEMIES = {
    "tutorial": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "rogue sheep",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": "Melee", "Strong against": "None"},
         "Moves": [
             {"Move name": "Bash", "Base damage": 2, "Type": "None", "Stamina use": 0},
         ]
         }
    ]},
    "main road 1": {"Max num of enemies": 2, "Min num of enemies": 2, "Enemies": [
        {"Name": "goblin with a sword",
         "Stats": {"Health": 15, "Stamina": 5, "Weakness": "Ranged", "Strong against": "None"},
         "Moves": [
             {"Move name": "Weak cut", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Cut", "Base damage": 4, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Throw sword", "Base damage": 2, "Type": "Ranged", "Stamina use": 2}
         ]
         },
        {"Name": "goblin with a bow",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": "Melee", "Strong against": "None"},
         "Moves": [
             {"Move name": "Shoot an arrow", "Base damage": 2, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Shoot 2 arrows", "Base damage": 4, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Shoot 3 arrows", "Base damage": 6, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]},
    "forest 1": {"Max num of enemies": 3, "Min num of enemies": 3, "Enemies": [
        {"Name": "wolf",
         "Stats": {"Health": 8, "Stamina": 4, "Weakness": "Ranged", "Strong against": "None"},
         "Moves": [
             {"Move name": "Scratch", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Bite", "Base damage": 4, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Gnaw", "Base damage": 6, "Type": "Melee", "Stamina use": 2}
         ]
         }
    ]},
    "Area test 1": {"Max num of enemies": 3, "Enemies": [
        {"Name": "test1",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 3, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 6, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 9, "Type": "Melee", "Stamina use": 2}
         ]
         },
        {"Name": "test2",
         "Stats": {"Health": 20, "Stamina": 10, "Weakness": "Melee", "Strong against": "Ranged"},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 3, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 6, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 9, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]},
    "Area test 2": {"Max num of enemies": 3, "Enemies": [
        {"Name": "test3",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": "Melee", "Strong against": "Melee"},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 6, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 9, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 12, "Type": "Melee", "Stamina use": 2}
         ]
         },
        {"Name": "test4",
         "Stats": {"Health": 20, "Stamina": 10, "Weakness": "Ranged", "Strong against": "Melee"},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 6, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 9, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 12, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]}
}

# variables
player_area = "tutorial"

player_money = 0

player_level = 1

# ----------------------- Functions -----------------------
def quit_game():
    print("Quitting game")
    time.sleep(1)
    quit()


def enter_to_continue():
    print()
    choice = input("Press enter to continue: ")
    choice.lower()
    if choice == "quit":
        quit()
    print()


def damage_calculate(thing, move, turn):
    if turn == "Player":
        print("---------------------")
        print("You are attacking", thing["Name"], "with", move["Move name"])
    else:
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("The enemy is attacking with", move["Move name"])




    if turn == "Player":
        if move["Type"] == thing["Stats"]["Weakness"]:
            print("Super effective")
            damage_multiplier = DAMAGE_VALUES["Strong"]
        elif move["Type"] == thing["Stats"]["Strong against"]:
            damage_multiplier = DAMAGE_VALUES["Weak"]
            print("Not effective")
        else:
            damage_multiplier = DAMAGE_VALUES["Normal"]
    else:
        if move["Type"] in player_equipment["Armour"]["Weakness"]:
            print("Super effective")
            damage_multiplier = DAMAGE_VALUES["Strong"]
        elif move["Type"] in player_equipment["Armour"]["Strong against"]:
            damage_multiplier = DAMAGE_VALUES["Weak"]
            print("Not effective")
        else:
            damage_multiplier = DAMAGE_VALUES["Normal"]

    if turn == "Player":
        damage = (player_stats["Stats"]["Strength"] * move["Base damage"] * damage_multiplier) + player_stats["Stats"]["Bonus damage"]
        print(move["Move name"], "did", damage, "damage to the enemy")
    else:
        damage = (move["Base damage"] * damage_multiplier) / thing["Stats"]["Defense"]
        print(move["Move name"], "did", damage, "damage to you")



    thing["Stats"]["Health"] = thing["Stats"]["Health"] - damage


    if turn == "Player":
        print("Enemy is at", thing["Stats"]["Health"], "health")
        print("---------------------")
    else:
        print("You are at", thing["Stats"]["Health"], "health")
        print("~~~~~~~~~~~~~~~~~~~~~")

    enter_to_continue()


def battle(area):
    print()

    print("You are in a battle")

    # set up battle

    # isolates the player stats list
    player = copy.deepcopy(player_stats)

    enter_to_continue()

    # random enemy generation
    num_enemy = random.randint(POSSIBLE_ENEMIES[area]["Min num of enemies"], POSSIBLE_ENEMIES[area]["Max num of enemies"])
    enemies = []

    # adds the enemies to a list and prints out the names
    for i in range(0, num_enemy):
        enemies.append(copy.deepcopy(POSSIBLE_ENEMIES[area]["Enemies"][random.randint(0, len(POSSIBLE_ENEMIES[area]["Enemies"]) - 1)]))
        print("A", enemies[i]["Name"], "appeared")

    enter_to_continue()

    while True:
        if player["Stats"]["Health"] > 0:
            # Your turn
            print("Your turn")
            print("----------")
            enter_to_continue()

            print("Enemy info")

            for i in range(0, len(enemies)):
                print("---------------")
                print("Name: ", enemies[i]["Name"])
                print("Health: ", enemies[i]["Stats"]["Health"])
            print("---------------")

            print()
            print("Your stats: ")
            print("---------------")
            print("Health: ", player["Stats"]["Health"])
            print("Stamina: ", player["Stats"]["Stamina"])
            print("---------------")

            enter_to_continue()

            print("Your moves: ")
            print("---------------")

            weapon_info = player_equipment["Weapon"]["Info"]
            # move selection
            for i in range(0, len(weapon_info)):
                print("Type", i + 1, "for")
                print(weapon_info[i]["Move name"], "| Damage -", weapon_info[i]["Base damage"],
                      "| Hit multiple enemies -", weapon_info[i]["Hit multi enemy"], "| Stamina cost -",
                      weapon_info[i]["Stamina use"], "| Move type -", weapon_info[i]["Type"])

                if i == len(weapon_info) - 1:
                    print()
                    print("Type", i + 2, "for")
                    print("Rest and gain 5 stamina")
                    print("---------------")
                print()

            while True:
                choose_move = input("Choose move: ")
                try:
                    choose_move = int(choose_move)
                    if choose_move >= 1 and choose_move <= len(weapon_info) + 1:
                        choose_move = choose_move - 1

                        if choose_move > len(weapon_info) - 1:
                            choose_move = "Rest"
                            break
                        else:
                            choose_move = player_equipment["Weapon"]["Info"][choose_move]
                            if (player["Stats"]["Stamina"] - choose_move["Stamina use"]) >= 0:
                                break
                            else:
                                print("Not enough stamina to use this move")
                    else:
                        print("Not a valid move")
                except ValueError:
                    if choose_move.lower() == "quit":
                        quit_game()
                    else:
                        print("Not a number")

            # gain stamina or enemy selection

            if choose_move == "Rest":
                print("You rested")
                print("You gained 5 stamina")
                player["Stats"]["Stamina"] += 5
                print("You are at", player["Stats"]["Stamina"], "stamina")
                print()
            else:

                # enemy selection

                target = []

                if choose_move["Hit multi enemy"] == False and len(enemies) > 1:
                    for i in range(0, len(enemies)):
                        print("Type", i + 1, "to attack", enemies[i]["Name"])

                    while True:
                        choose_target = input("Choose enemy: ")
                        try:
                            choose_target = int(choose_target)
                            if choose_target >= 1 and choose_target <= len(enemies):
                                target.append([enemies[choose_target - 1]])
                                break
                            else:
                                print("Not a valid enemy")
                        except ValueError:
                            if choose_target.lower() == "quit":
                                quit_game()
                            else:
                                print("Not a valid input")

                elif len(enemies) == 1:
                    target.append([enemies[0]])

                elif choose_move["Hit multi enemy"] == True and len(enemies) >= 2:
                    for i in range(0, len(enemies)):
                        target.append([enemies[i]])

                print()
                print(choose_move["Move name"], "used", choose_move["Stamina use"], "stamina")
                player["Stats"]["Stamina"] = player["Stats"]["Stamina"] - choose_move["Stamina use"]
                print("You are at", player["Stats"]["Stamina"], "stamina")

                enter_to_continue()

                # damage calc

                # check weakness
                # add to damage multiplier

                # change enemy health
                # print enemy health

                # end player turn

                # damage calc. Runs the code for every enemy in the target list
                # print out all the information need
                # based on the strength and weakness and typing it will get a multiplier
                # will remove the health off the enemy

                for i in range(0, len(target)):
                    damage_calculate(target[i][0], choose_move, "Player")
                    # after damage calculation it checks if it is dead and if it is it will remove it from the enemies list
                    if target[i][0]["Stats"]["Health"] <= 0:
                        enemies.remove(target[i][0])

        if len(enemies) == 0:
            print("Battle win")
            enter_to_continue()
            break

        print("Enemies turn")
        enter_to_continue()

        # enemy ai
        for i in range(0, len(enemies)):

            # enemy ai for 1 enemy

            # check if enemy is alive

            enemy = enemies[i]
            if enemy["Stats"]["Health"] > 0:
                random_move_num = random.randint(0, len(enemy["Moves"]) - 1)

                # check stamina and choose a move
                if enemy["Moves"][random_move_num]["Stamina use"] <= enemy["Stats"]["Stamina"]:
                    enemy_move = enemy["Moves"][random_move_num]
                else:
                    enemy_move = enemy["Moves"][0]  # move 1 or 0 stamina use is always at 0

                enemy["Stats"]["Stamina"] = enemy["Stats"]["Stamina"] - enemy_move["Stamina use"]

                damage_calculate(player, enemy_move, "Enemy")

        # check if player is dead and if so breaks the function
        if player["Stats"]["Health"] <= 0:
            print("You lose")
            enter_to_continue()
            break

# answers is a list
def int_error_detection(question, answers):
    while True:
        player_input = input(question)
        try:
            player_input = int(player_input)

            if player_input in answers:
                return player_input
            else:
                print("Not a choice")

        except ValueError:
            if player_input.lower() == "quit":
                quit_game()
            else:
                print("Not an integer")


# ----------------------- Main code -----------------------

print("Start game")

# while loop that checks if you want to play the game. Possible answers are yes or no, if input something else the loop will ask you to try again
while True:
    try:
        start_choice = str(input("yes/no: "))
        start_choice = start_choice.lower()
        if start_choice == "yes" or start_choice == "y":
            start_choice = "yes"
            break
        elif start_choice == "no" or start_choice == "n":
            start_choice = "no"
            break
        else:
            print("Not a valid string")
    except ValueError:
        print("Not a valid input")

# Code for quiting the game. Checks if the answer is no then runs the quit function
if start_choice == "no":
    quit_game()

print("Welcome")
print("Infomation")
print("You can type quit at any of the inputs to quit the program")
enter_to_continue()

print("You are on a quest to destroy a ring")
print("You must venture to Mount Dooom where you can destroy the ring")

enter_to_continue()

print("Choose your character")
print()

# for loop that prints out the possible classes and another for loop for lists out want input for which class to choose
for i in range(len(POSSIBLE_CLASSES)):
    print("Character", i + 1, ":", POSSIBLE_CLASSES[i]["Name"])
    print("Stats: ")
    print("| Health:", POSSIBLE_CLASSES[i]["Stats"]["Health"], "| Base damage:", POSSIBLE_CLASSES[i]["Stats"]["Bonus damage"],
          "| Defense:", POSSIBLE_CLASSES[i]["Stats"]["Defense"], "| Strength:", POSSIBLE_CLASSES[i]["Stats"]["Strength"],
          "| Stamina:", POSSIBLE_CLASSES[i]["Stats"]["Stamina"])
    print()

print()

for i in range(len(POSSIBLE_CLASSES)):
    print("Type", i + 1, "for", POSSIBLE_CLASSES[i]["Name"])

# another while loop with try and except. Asks for a which class using 1,2,3 etc.
# If input str or bool will run try and except and ask again. If number is too big or too small will ask fo input again.
while True:
    player_class_choice = input("Choose a character: ")
    try:
        player_class_choice = int(player_class_choice)
        if player_class_choice >= 1 and player_class_choice <= len(POSSIBLE_CLASSES):
            player_class_choice = player_class_choice - 1
            print("You choose: ", POSSIBLE_CLASSES[player_class_choice]["Name"])
            player_stats = POSSIBLE_CLASSES[player_class_choice]
            break
        else:
            print("Not a valid input")
    except ValueError:
        if player_class_choice.lower() == "quit":
            quit_game()
        else:
            print("Not an number")

enter_to_continue()

for x in range(0,len(POSSIBLE_WEAPONS[player_area])):
    print("Weapon", x + 1, ":", POSSIBLE_WEAPONS[player_area][x]["Name"])
    print("Moves: ")
    for y in range(0, len(POSSIBLE_WEAPONS[player_area][x]["Info"])):
        weapon_info = POSSIBLE_WEAPONS[player_area][x]["Info"][y]
        print(weapon_info["Move name"], "| Damage -", weapon_info["Base damage"],
              "| Hit multiple enemies -", weapon_info["Hit multi enemy"], "| Stamina cost -",
              weapon_info["Stamina use"], "| Move type -", weapon_info["Type"])
    print()
print()

for i in range(0,len(POSSIBLE_WEAPONS[player_area])):
    print("Type", i+1, "for", POSSIBLE_WEAPONS[player_area][i]["Name"])

while True:
    player_weapon_choice = input("Choose a weapon: ")
    try:
        player_weapon_choice = int(player_weapon_choice)
        if player_weapon_choice >= 1 and player_weapon_choice <= 3:
            player_weapon_choice = player_weapon_choice - 1
            print("You choose: ", POSSIBLE_WEAPONS[player_area][i]["Name"])
            player_equipment["Weapon"] = POSSIBLE_WEAPONS[player_area][player_weapon_choice]
            break
        else:
            print("Not a valid input")
    except ValueError:
        if player_weapon_choice.lower() == "quit":
            quit_game()
        else:
            print("Not an number")

print("You are currently at Hobbitown")
print("You travel down the road until a rogue sheep is blocking the way")


enter_to_continue()
battle(player_area)

print("Which way do you want to go")
print("Type 1 to follow the main road and fight the group of goblins, type 2 to go around them through the forest")

one_use_answer = int_error_detection(": ", [1,2])
if one_use_answer == 1:
    print("You chose to follow the main road")
    player_area = "main road 1"
elif one_use_answer == 2:
    print("You decided to go through the forest")
    player_area = "forest 1"
else:
    print("error")

enter_to_continue()
battle(player_area)

if player_area == "forest 1":
    print("You decided to go back on the road")
    player_area = "main road"