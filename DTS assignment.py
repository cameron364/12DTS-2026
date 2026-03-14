# DTS assignment ----- 11/3/26 ----- Cameron Christie

# ----------------------- Library -----------------------
import time
import random



# ----------------------- Variables -----------------------

# Dictionaries and lists
player_stats = {}

player_equipment = {
    "Weapon": {
        "Name": "Wooden Sword",
        "Info": [
            {"Move name": "Move 1", "Base damage": 2, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
            {"Move name": "Move 2", "Base damage": 1, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
            {"Move name": "Move 3", "Base damage": 4, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
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
    {"Name": "test1", "Health": 5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"},
    {"Name": "test2", "Health": 5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"},
    {"Name": "test3", "Health": 5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5, "Weakness": "Melee", "Strong against": "Ranged"}
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
    "tutorial": [
        {"Name": "test1",
        "Stats" : {"Health": 10, "Stamina" : 5, "Weakness": "Melee", "Strong against": "Ranged"},
        "Move 1": {"Base damage": 3, "Type" : "Melee", "Stamina use": 0},
        "Move 2": {"Base damage": 6, "Type" : "Melee", "Stamina use": 1},
        "Move 3": {"Base damage": 9, "Type" : "Melee", "Stamina use": 2}},
        {"Name": "test2",
        "Stats" : {"Health": 20, "Stamina" : 10, "Weakness": "Melee", "Strong against": "Ranged"},
        "Move 1": {"Base damage": 6, "Type" : "Ranged", "Stamina use": 0},
        "Move 2": {"Base damage": 9, "Type" : "Ranged", "Stamina use": 2},
        "Move 3": {"Base damage": 12, "Type" : "Ranged", "Stamina use": 4}}
    ],
    "Area test 1": [
        {"Name": "test3",
        "Stats" : {"Health": 10, "Stamina" : 5, "Weakness": "Melee", "Strong against": "Melee"},
        "Move 1": {"Base damage": 3, "Type" : "Melee", "Stamina use": 0},
        "Move 2": {"Base damage": 6, "Type" : "Melee", "Stamina use": 1},
        "Move 3": {"Base damage": 9, "Type" : "Melee", "Stamina use": 2}},
        {"Name": "test4",
        "Stats" : {"Health": 20, "Stamina" : 10, "Weakness": "Ranged", "Strong against": "Melee"},
        "Move 1": {"Base damage": 6, "Type" : "Ranged", "Stamina use": 0},
        "Move 2": {"Base damage": 9, "Type" : "Ranged", "Stamina use": 2},
        "Move 3": {"Base damage": 12, "Type" : "Ranged", "Stamina use": 4}}
    ]
}

# variables
player_area = "tutorial"




# ----------------------- Functions -----------------------
def enter_to_continue():
    print()
    input("Enter to continue: ")
    print()

def battle(area):

    # set up battle
    enter_to_continue()

    # random enemy generation
    num_enemy = random.randint(1, 3)
    enemies = []

    # adds the enemies to a list and prints out the names
    for i in range(0, num_enemy):
        enemies.append(POSSIBLE_ENEMIES[area][random.randint(0,len(POSSIBLE_ENEMIES[area])-1)])
        print("A", enemies[i]["Name"], "appeared")

    enter_to_continue()

    while True:
        while player_stats["Health"] > 0:
            # Your turn
            print("Your turn")
            print()


            print("Enemy info")

            for i in range(0, num_enemy):
                print("---------------")
                print("Name: ", enemies[i]["Name"])
                print("Health: ", enemies[i]["Stats"]["Health"])
            print("---------------")

            print()
            print("Your stats: ")
            print("Health: ", player_stats["Health"])
            print("Stamina: ", player_stats["Stamina"])
            print()

            print("Your moves: ")

            weapon_info = player_equipment["Weapon"]["Info"]
            print(len(weapon_info))
            # move selection
            for i in range(0, len(weapon_info)):
                print("Type", i+1, "for")
                print(weapon_info[i]["Move name"], "| Damage -", weapon_info[i]["Base damage"],
                      "| Hit multiple enemies -", weapon_info[i]["Hit multi enemy"], "| Stamina cost -",
                      weapon_info[i]["Stamina use"])
                print()

            while True:
                try:
                    choose_move = int(input("Choose move: "))
                    if choose_move >= 1 and choose_move <= len(weapon_info):
                        choose_move = choose_move - 1
                        choose_move = player_equipment["Weapon"]["Info"][choose_move]
                        break
                    else:
                        print("Not a valid move")
                except ValueError:
                    print("Not a valid input")

            # enemy selection

            for i in range(0,len(weapon_info)):
                pass

            target = []

            if choose_move["Hit multi enemy"] == False and num_enemy > 1:
                for i in range(0, num_enemy):
                    print("Type",i+1 , "to attack", enemies[i]["Name"])

                while True:
                    try:
                        choose_target = int(input("Choose enemy: "))
                        if choose_target >= 1 and choose_target <= num_enemy:
                            target.append([enemies[choose_target - 1]])
                            break
                        else:
                            print("Not a valid enemy")
                    except ValueError:
                        print("Not a valid input")

            elif num_enemy == 1:
                target.append([enemies[0]])

            elif choose_move["Hit multi enemy"] == True and num_enemy >= 2:
                for i in range(0,num_enemy):
                    target.append([enemies[i]])

            print()
            print(choose_move["Move name"], "used", choose_move["Stamina use"], "stamina")
            player_stats["Stamina"] = player_stats["Stamina"] - choose_move["Stamina use"]
            print("You are at", player_stats["Stamina"], "stamina")

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

            damage_multiplier = []
            damage = 0

            for i in range(0,len(target)):
                print("---------------------")
                print("You are attacking", target[i][0]["Name"], "with", choose_move["Move name"])
                if choose_move["Type"] == target[i][0]["Stats"]["Weakness"]:
                    print("Super effective")
                    damage_multiplier.append(DAMAGE_VALUES["Strong"])
                elif choose_move["Type"] == target[i][0]["Stats"]["Strong against"]:
                    damage_multiplier.append(DAMAGE_VALUES["Weak"])
                    print("Not effective")
                else:
                    damage_multiplier.append(DAMAGE_VALUES["Normal"])

                damage = player_stats["Strength"] * choose_move["Base damage"] * damage_multiplier[i]

                print(choose_move["Move name"], "did", damage, "damage to", target[i][0]["Name"])

                target[i][0]["Stats"]["Health"] = target[i][0]["Stats"]["Health"] - damage

                print(target[i][0]["Name"], "is at", target[i][0]["Stats"]["Health"], "health")
                print("---------------------")
                enter_to_continue()

            break
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
    print("| Health:", POSSIBLE_CLASSES[i]["Health"], "| Damage:", POSSIBLE_CLASSES[i]["Damage"],
          "| Defense:", POSSIBLE_CLASSES[i]["Defense"], "| Strength:", POSSIBLE_CLASSES[i]["Strength"],
          "| Stamina:", POSSIBLE_CLASSES[i]["Stamina"], "| Weakness:", POSSIBLE_CLASSES[i]["Weakness"],
          "| Strong against:", POSSIBLE_CLASSES[i]["Strong against"], "|"
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

print("print narrative and stuff here")

battle(player_area)