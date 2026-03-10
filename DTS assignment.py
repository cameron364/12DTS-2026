# DTS assignment ----- 10/3/26 ----- Cameron Christie

# ----------------------- Library -----------------------
import time
import random



# ----------------------- Variables -----------------------
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

POSSIBLE_CLASSES = {
    "test1": {"Health":5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5},
    "test2": {"Health":5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5},
    "test3": {"Health":5, "Damage": 5, "Defense":0.5, "Strength":0.5, "Stamina": 5}
}

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
        "Stats" : {"Health": 10, "Stamina" : 5, "Weakness": "Melee"}
        "Move 1": {"Base damage": 3, "Type" : "Melee", "Stamina use": 0},
        "Move 2": {"Base damage": 6, "Type" : "Melee", "Stamina use": 1},
        "Move 3": {"Base damage": 9, "Type" : "Melee", "Stamina use": 2}
    },
    "test2" : {
        "Stats" : {"Health": 20, "Stamina" : 10, "Weakness": "Ranged"}
        "Move 1": {"Base damage": 6, "Type" : "Ranged", "Stamina use": 0},
        "Move 2": {"Base damage": 9, "Type" : "Ranged", "Stamina use": 2},
        "Move 3": {"Base damage": 12, "Type" : "Ranged", "Stamina use": 4}
    }
}





# ----------------------- Functions -----------------------
def create_player_stats(player_class):
    global player_stats
    if player_class == possible_classes["test1"]:
        player_stats = possible_classes["test1"]

    elif player_class == possible_classes["test2"]:
        player_stats = possible_classes["test2"]

    elif player_class == possible_classes["test2"]:
        player_stats = possible_classes["test2"]





# ----------------------- Main code -----------------------
