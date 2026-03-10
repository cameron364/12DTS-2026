# DTS assignment ----- 10/3/26 ----- Cameron Christie

# ----------------------- Library -----------------------
import time
import random



# ----------------------- Variables -----------------------

# Dictionaries and lists
player_stats = {
    "Health",
    "Damage",
    "Defense",
    "Strength",
    "Stamina"
}

player_equipment = {
    "Weapon",
    "Armour"
}

inventory = []

POSSIBLE_CLASSES = [
    {"Name": "test1", "Health": 5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5},
    {"Name": "test2", "Health": 5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5},
    {"Name": "test3", "Health": 5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5}
]

POSSIBLE_WEAPONS = {
    "Sword": {
        "Type": "i dont know",
        "Move 1": {"Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
        "Move 2": {"Base damage": 2, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
        "Move 3": {"Base damage": 7, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
    },
    "Bow": {
        "Type": "i dont know",
        "Move 1": {"Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 1},
        "Move 2": {"Base damage": 2, "Hit multi enemy": True, "Type": "Ranged", "Stamina use": 2},
        "Move 3": {"Base damage": 7, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3}
    }
}

POSSIBLE_ARMOUR = {
    "Chainmail": {
        "Defense": 5,
        "Weakness": "Range"
    },
    "Knights armour": {
        "Defense": 10,
        "Weakness": "Melee"
    }
}

POSSIBLE_ENEMIES = {
    "test1" : {
        "Stats" : {"Name": "test1", "Health": 10, "Stamina" : 5, "Weakness": "Melee"},
        "Move 1": {"Base damage": 3, "Type" : "Melee", "Stamina use": 0},
        "Move 2": {"Base damage": 6, "Type" : "Melee", "Stamina use": 1},
        "Move 3": {"Base damage": 9, "Type" : "Melee", "Stamina use": 2}
    },
    "test2" : {
        "Stats" : {"Name": "test2", "Health": 20, "Stamina" : 10, "Weakness": "Ranged"},
        "Move 1": {"Base damage": 6, "Type" : "Ranged", "Stamina use": 0},
        "Move 2": {"Base damage": 9, "Type" : "Ranged", "Stamina use": 2},
        "Move 3": {"Base damage": 12, "Type" : "Ranged", "Stamina use": 4}
    }
}



# variables


# ----------------------- Functions -----------------------
def create_player_stats(player_class):
    global player_stats
    if player_class == POSSIBLE_CLASSES["test1"]:
        player_stats = POSSIBLE_CLASSES["test1"]

    elif player_class == POSSIBLE_CLASSES["test2"]:
        player_stats = POSSIBLE_CLASSES["test2"]

    elif player_class == POSSIBLE_CLASSES["test2"]:
        player_stats = POSSIBLE_CLASSES["test2"]

def enter_to_continue():
    input("Enter to continue: ")
    print()



# ----------------------- Main code -----------------------

print("Start game")

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

if start_choice == "no":
    print("Quitting game")
    time.sleep(1)
    quit()

print("Welcome")
enter_to_continue()

print("Choose class")
print()

for i in range(len(POSSIBLE_CLASSES)):
    print("Class", i+1, ":", POSSIBLE_CLASSES[i]["Name"])
    print("Stats: ")
    print("| Health:", POSSIBLE_CLASSES[i]["Health"], "| Damage:", POSSIBLE_CLASSES[i]["Damage"],
          "| Defense:", POSSIBLE_CLASSES[i]["Defense"], "| Strength:", POSSIBLE_CLASSES[i]["Strength"],
          "| Stamina:", POSSIBLE_CLASSES[i]["Stamina"], " |"
          )
    print()

print()

for i in range(len(POSSIBLE_CLASSES)):
    print("Type", i+1, "for", POSSIBLE_CLASSES[i]["Name"])

while True:
    try:
        player_class_choice = int(input("Choose a class: "))
        if player_class_choice >= 1 and player_class_choice <= len(POSSIBLE_CLASSES):
            player_class_choice = player_class_choice - 1
            break
        else:
            print("Not a valid input")

    except ValueError:
        print("Not a valid input")

