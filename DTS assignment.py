# DTS assignment ----- 24/3/26 ----- Cameron Christie

# ----------------------- Library -----------------------
import time
import random
import copy



# ----------------------- Variables -----------------------

# Dictionaries and lists
player_stats = {}

player_equipment = {
    "Weapon": {
        "Name": "Wooden Sword",
        "Info": [
            {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
            {"Move name": "Move 2", "Base damage": 5, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
            {"Move name": "Move 3", "Base damage": 10, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
        ]
    },

    "Armour": {
        "Name": "Wooden Armour",
        "Defense": 2,
        "Weakness": "Both"}
}

inventory = []

DAMAGE_VALUES = {"Normal": 1, "Strong": 2, "Weak": 0.5}

POSSIBLE_CLASSES = [
    {"Name": "player test1", "Stats": {"Health": 20, "Damage": 5, "Defense": 1, "Strength": 1, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"}},
    {"Name": "player test2", "Stats": {"Health": 20, "Damage": 5, "Defense": 1, "Strength": 1, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"}},
    {"Name": "player test3", "Stats": {"Health": 20, "Damage": 5, "Defense": 1, "Strength": 1, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"}}
]

POSSIBLE_WEAPONS = [
    {
        "Name": "Sword",
        "Info": [
            {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
            {"Move name": "Move 2", "Base damage": 2, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
            {"Move name": "Move 3", "Base damage": 7, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
        ]
    },
    {
        "Name": "Bow",
        "Info": [
            {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 1},
            {"Move name": "Move 2", "Base damage": 2, "Hit multi enemy": True, "Type": "Ranged", "Stamina use": 2},
            {"Move name": "Move 3", "Base damage": 7, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3}
        ]
    },
]

POSSIBLE_ARMOUR = [
    {
        "Name": "Chainmail",
        "Defense": 5,
        "Weakness": "Range"
    },
    {
        "Name": "Knights Armour",
        "Defense": 10,
        "Weakness": "Melee"
    }
]

POSSIBLE_ENEMIES = {
    "tutorial": {"Num of enemies": 1, "Enemies": [
            {"Name": "sheep",
                "Stats": {"Health": 10, "Stamina": 5, "Weakness": "Melee", "Strong against": "None"},
                 "Moves": [
                    {"Move name": "Move 1", "Base damage": 2, "Type": "None", "Stamina use": 0},
                ]
            }
    ]},
    "Area test 1": {"Num of enemies": 3, "Enemies": [
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
    "Area test 2": {"Num of enemies": 3, "Enemies": [
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




# ----------------------- Functions -----------------------
def enter_to_continue():
    print()
    input("Press enter to continue: ")
    print()

def damage_calculate(thing, move, turn):
    if turn == "Player":
        print("---------------------")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~")

    print("You are attacking", thing["Name"], "with", move["Move name"])

    if move["Type"] == thing["Stats"]["Weakness"]:
        print("Super effective")
        damage_multiplier = DAMAGE_VALUES["Strong"]
    elif move["Type"] == thing["Stats"]["Strong against"]:
        damage_multiplier = DAMAGE_VALUES["Weak"]
        print("Not effective")
    else:
        damage_multiplier = DAMAGE_VALUES["Normal"]

    if turn == "Player":
        damage = player_stats["Stats"]["Strength"] * move["Base damage"] * damage_multiplier
    else:
        damage = (move["Base damage"] * damage_multiplier) / thing["Stats"]["Defense"]

    print(move["Move name"], "did", damage, "damage to", thing["Name"])

    thing["Stats"]["Health"] = thing["Stats"]["Health"] - damage

    print(thing["Name"], "is at", thing["Stats"]["Health"], "health")
    if turn == "Player":
        print("---------------------")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~")

    enter_to_continue()

def battle(area):
    for i in range(0,20):
        print()

    print("You are in a battle")

    # set up battle

    # isolates the player stats list
    player = copy.deepcopy(player_stats)

    enter_to_continue()

    # random enemy generation
    num_enemy = random.randint(1, POSSIBLE_ENEMIES[area]["Num of enemies"])
    enemies = []

    # adds the enemies to a list and prints out the names
    for i in range(0, num_enemy):
        enemies.append(copy.deepcopy(POSSIBLE_ENEMIES[area]["Enemies"][random.randint(0,len(POSSIBLE_ENEMIES[area]["Enemies"])-1)]))
        print("A", enemies[i]["Name"], "appeared")

    enter_to_continue()

    while True:
        if player["Stats"]["Health"] > 0:
            # Your turn
            print("Your turn")
            print("----------")
            print()


            print("Enemy info")

            for i in range(0, len(enemies)):
                print("---------------")
                print("Name: ", enemies[i]["Name"])
                print("Health: ", enemies[i]["Stats"]["Health"])
            print("---------------")

            print()
            print("Your stats: ")
            print("Health: ", player["Stats"]["Health"])
            print("Stamina: ", player["Stats"]["Stamina"])
            print()

            enter_to_continue()

            print("Your moves: ")
            print()

            weapon_info = player_equipment["Weapon"]["Info"]
            # move selection
            for i in range(0, len(weapon_info)):
                print("Type", i+1, "for")
                print(weapon_info[i]["Move name"], "| Damage -", weapon_info[i]["Base damage"],
                      "| Hit multiple enemies -", weapon_info[i]["Hit multi enemy"], "| Stamina cost -",
                      weapon_info[i]["Stamina use"])
                if i == len(weapon_info)-1:
                    print()
                    print("Type", i+2, "for")
                    print("Rest and gain 5 stamina")
                print()



            while True:
                try:
                    choose_move = int(input("Choose move: "))
                    if choose_move >= 1 and choose_move <= len(weapon_info)+1:
                        choose_move = choose_move - 1

                        if choose_move > len(weapon_info)-1:
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
                    print("Not a valid input")

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
                        print("Type",i+1 , "to attack", enemies[i]["Name"])

                    while True:
                        try:
                            choose_target = int(input("Choose enemy: "))
                            if choose_target >= 1 and choose_target <= len(enemies):
                                target.append([enemies[choose_target - 1]])
                                break
                            else:
                                print("Not a valid enemy")
                        except ValueError:
                            print("Not a valid input")

                elif len(enemies) == 1:
                    target.append([enemies[0]])

                elif choose_move["Hit multi enemy"] == True and len(enemies) >= 2:
                    for i in range(0,len(enemies)):
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



                for i in range(0,len(target)):
                    damage_calculate(target[i][0], choose_move, "Player")

        # enemy check health and if below zero removes from choices
        # updates num of enemy to correct enemies
        for i in range(0, len(enemies)):
            enemy = enemies[len(enemies)-1-i]
            if enemy["Stats"]["Health"] <= 0:
                enemies.remove(enemy)

        if len(enemies) == 0:
            print("Battle win")
            enter_to_continue()
            break

        print("Enemies turn")
        enter_to_continue()


        # enemy ai
        for i in range(0,len(enemies)):

            # enemy ai for 1 enemy

            # check if enemy is alive

            enemy = enemies[i]
            if enemy["Stats"]["Health"] > 0:
                random_move_num = random.randint(0,len(enemy["Moves"])-1)

                # check stamina and choose a move
                if enemy["Moves"][random_move_num]["Stamina use"] <= enemy["Stats"]["Stamina"]:
                    enemy_move = enemy["Moves"][random_move_num]
                else:
                    enemy_move = enemy["Moves"][0] # move 1 or 0 stamina use is always at 0

                enemy["Stats"]["Stamina"] = enemy["Stats"]["Stamina"] - enemy_move["Stamina use"]

                damage_calculate(player, enemy_move, "Enemy")


        # check if player is dead and if so breaks the function
        if player["Stats"]["Health"] <= 0:
            print("You lose")
            enter_to_continue()
            break









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
    print("Quitting game")
    time.sleep(1)
    quit()

print("Welcome")
enter_to_continue()

print("Choose class")
print()

# for loop that prints out the possible classes and another for loop for lists out want input for which class to choose
for i in range(len(POSSIBLE_CLASSES)):
    print("Class", i+1, ":", POSSIBLE_CLASSES[i]["Name"])
    print("Stats: ")
    print("| Health:", POSSIBLE_CLASSES[i]["Stats"]["Health"], "| Damage:", POSSIBLE_CLASSES[i]["Stats"]["Damage"],
          "| Defense:", POSSIBLE_CLASSES[i]["Stats"]["Defense"], "| Strength:", POSSIBLE_CLASSES[i]["Stats"]["Strength"],
          "| Stamina:", POSSIBLE_CLASSES[i]["Stats"]["Stamina"], "| Weakness:", POSSIBLE_CLASSES[i]["Stats"]["Weakness"],
          "| Strong against:", POSSIBLE_CLASSES[i]["Stats"]["Strong against"], "|"
          )
    print()

print()

for i in range(len(POSSIBLE_CLASSES)):
    print("Type", i+1, "for", POSSIBLE_CLASSES[i]["Name"])

# another while loop with try and except. Asks for a which class using 1,2,3 etc.
# If input str or bool will run try and except and ask again. If number is too big or too small will ask fo input again.
while True:
    try:
        player_class_choice = int(input("Choose a class: "))
        if player_class_choice >= 1 and player_class_choice <= len(POSSIBLE_CLASSES):
            player_class_choice = player_class_choice - 1
            print("You choose: ", POSSIBLE_CLASSES[player_class_choice]["Name"])
            player_stats = POSSIBLE_CLASSES[player_class_choice]
            break
        else:
            print("Not a valid input")

    except ValueError:
        print("Not a valid input")

print("story uisuibsdfaufiubfuibdsfiubdfibdfibdbifiibfibfdib")

battle(player_area)


