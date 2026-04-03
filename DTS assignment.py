# DTS assignment ----- 1/4/26 ----- Cameron Christie

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
        "Name": "Basic Armour",
        "Weakness": ["None"],
        "Strong against": ["None"],
        "Cost": 5
    }
}

player_spare_equipment = {
    "Weapons": [],
    "Armour": []
}

player_drop_inventory = []

item_inventory = []

DAMAGE_VALUES = {"Normal": 1, "Strong": 2, "Weak": 0.5}

POSSIBLE_ITEMS = {
    "Shop 1": [
        {"Name": "Apple", "Healing amount": 5, "Cost": 5},
        {"Name": "Banana", "Healing amount": 7, "Cost": 7},
    ],
    "Shop 2": [
        {"Name": "Big apple", "Healing amount": 15, "Cost": 10},
        {"Name": "Big banana", "Healing amount": 20, "Cost": 15},
        {"Name": "Big apple and big banana", "Healing amount": 35, "Cost": 20}
    ]
}

POSSIBLE_CLASSES = [
    {"Name": "Knight",
     "Stats": {"Health": 20, "Bonus damage": 5, "Defense": 2, "Strength": 1, "Stamina": 8}},
    {"Name": "Wizard",
     "Stats": {"Health": 15, "Bonus damage": 10, "Defense": 1, "Strength": 0.5, "Stamina": 20}},
    {"Name": "Warrior",
     "Stats": {"Health": 30, "Bonus damage": 1, "Defense": 1, "Strength": 2, "Stamina": 10}}
]

POSSIBLE_WEAPONS = {
    "tutorial": [
        {"Name": "Starter Sword", "Cost": 5,
            "Info": [
                {"Move name": "Stab", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Slash", "Base damage": 2, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Jab", "Base damage": 4, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2}]},
        {"Name": "Starter Wand", "Cost": 5,
            "Info": [
                {"Move name": "Zap", "Base damage": 6, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Fireball", "Base damage": 5, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3},
                {"Move name": "Poke", "Base damage": 2, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1}]},
        {"Name": "Starter Axe", "Cost": 5,
            "Info": [
                {"Move name": "Cut", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Axe spin", "Base damage": 5, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 3},
                {"Move name": "Throw axe", "Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2}
            ]}
    ],
    "Shop 1": [
        {"Name": "Fire sword", "Cost": 10,
            "Info": [
                {"Move name": "Powerful stab", "Base damage": 10, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Powerful slash", "Base damage": 6, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Powerful jab", "Base damage": 8, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3},
                {"Move name": "Fire stab", "Base damage": 6, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 3}
            ]},
        {"Name": "Wand", "Cost": 10,
            "Info": [
                {"Move name": "Strong zap", "Base damage": 12, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Strong fireball", "Base damage": 10, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3},
                {"Move name": "Powerful poke", "Base damage": 4, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3},
                {"Move name": "Stab", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 2}
            ]}
    ],
    "part 2 encounter": [
        {"Name": "Legendary rock sword", "Cost": 50,
            "Info": [
                {"Move name": "Super powerful stab", "Base damage": 20, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Super powerful slash", "Base damage": 12, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Super powerful jab", "Base damage": 16, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2},
                {"Move name": "Heavy rock attack", "Base damage": 20, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Heavy rock fall", "Base damage": 20, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3}
            ]},
        {"Name": "Legendary snow sword", "Cost": 50,
            "Info": [
                {"Move name": "Super powerful stab", "Base damage": 20, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Super powerful slash", "Base damage": 12, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Super powerful jab", "Base damage": 16, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2},
                {"Move name": "Magic snowball", "Base damage": 20, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Magic avalanche", "Base damage": 20, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3}
            ]}
    ],
    "Shop 2": [
        {"Name": "Big bow", "Cost": 50,
            "Info": [
                {"Move name": "Powerful arrow shot", "Base damage": 18, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 1},
                {"Move name": "Arrow rain", "Base damage": 10, "Hit multi enemy": True, "Type": "Ranged", "Stamina use": 1},
                {"Move name": "Magic arrow", "Base damage": 18, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Arrow stab", "Base damage": 12, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 2}
            ]},
        {"Name": "Big sword", "Cost": 50,
            "Info": [
                {"Move name": "Super duper powerful stab", "Base damage": 26, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3},
                {"Move name": "Super duper powerful slash", "Base damage": 20, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 3},
                {"Move name": "Super duper powerful jab", "Base damage": 22, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3}
            ]},
        {"Name": "Big wand", "Cost": 50,
            "Info": [
                {"Move name": "Big zap", "Base damage": 22, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Big fireball", "Base damage": 20, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3},
                {"Move name": "Powerful jab", "Base damage": 16, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3},
                {"Move name": "Powerful stab", "Base damage": 18, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
            ]}
    ]
}

POSSIBLE_ARMOUR = {
    "Shop 1": [
    {
        "Name": "Chainmail",
        "Cost": 5,
        "Weakness": ["None"],
        "Strong against": ["Ranged"]
    },
    {
        "Name": "Magic cloak",
        "Cost": 5,
        "Weakness": [],
        "Strong against": ["Magic"]
    },
    {
        "Name": "Metal armour",
        "Cost": 5,
        "Weakness": [],
        "Strong against": ["Melee"]
    }],
    "Shop 2": [
        {
        "Name": "Strong armour",
        "Cost": 50,
        "Weakness": ["Magic"],
        "Strong against": ["Melee","Ranged"]
        },
        {
        "Name": "Strong cloak",
        "Cost": 50,
        "Weakness": ["Melee"],
        "Strong against": ["Magic","Ranged"]
        },
        {
        "Name": "Heavy armour",
        "Cost": 50,
        "Weakness": ["Ranged"],
        "Strong against": ["Melee","Magic"]
        }
    ]
}

POSSIBLE_ENEMIES = {
    "tutorial": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "stubborn rogue sheep",
         "Stats": {"Health": 30, "Stamina": 5, "Weakness": ["Melee","Ranged","Magic"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Bash", "Base damage": 1, "Type": "Melee", "Stamina use": 0},
         ]
         }
    ]},
    "main road 1": {"Max num of enemies": 2, "Min num of enemies": 2, "Enemies": [
        {"Name": "goblin with a sword",
         "Stats": {"Health": 15, "Stamina": 5, "Weakness": ["Ranged"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Weak cut", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Cut", "Base damage": 4, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Throw sword", "Base damage": 2, "Type": "Ranged", "Stamina use": 2}
         ]
         },
        {"Name": "goblin with a bow",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": ["Melee"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Shoot an arrow", "Base damage": 2, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Shoot 2 arrows", "Base damage": 4, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Shoot 3 arrows", "Base damage": 6, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]},
    "forest 1": {"Max num of enemies": 3, "Min num of enemies": 3, "Enemies": [
        {"Name": "wolf",
         "Stats": {"Health": 8, "Stamina": 4, "Weakness": ["Ranged"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Scratch", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Bite", "Base damage": 4, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Gnaw", "Base damage": 6, "Type": "Melee", "Stamina use": 2}
         ]
         }
    ]},
    "main road": {"Max num of enemies": 5, "Min num of enemies": 3, "Enemies": [
        {"Name": "goblin with a sword",
         "Stats": {"Health": 15, "Stamina": 5, "Weakness": ["Ranged"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Weak cut", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Cut", "Base damage": 4, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Throw sword", "Base damage": 2, "Type": "Ranged", "Stamina use": 2}
         ]
         },
        {"Name": "goblin with a bow",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": ["Melee"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Shoot an arrow", "Base damage": 2, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Shoot 2 arrows", "Base damage": 4, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Shoot 3 arrows", "Base damage": 6, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]},
    "main road final": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "Goblin Giant",
         "Stats": {"Health": 50, "Stamina": 8, "Weakness": ["Magic"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Punch", "Base damage": 4, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Smash", "Base damage": 6, "Type": "Melee", "Stamina use": 2},
             {"Move name": "Kick", "Base damage": 6, "Type": "Ranged", "Stamina use": 2}
         ]
         }
    ]},
    "cave 1": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "Golemite",
         "Stats": {"Health": 30, "Stamina": 0, "Weakness": ["Magic"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Rock smack", "Base damage": 8, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Rock fall", "Base damage": 8, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Magic rock attack", "Base damage": 8, "Type": "Magic", "Stamina use": 0}
         ]
         }
    ]},
    "mountain 1": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "Cougar",
         "Stats": {"Health": 25, "Stamina": 0, "Weakness": ["Ranged"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Vicious scratch", "Base damage": 10, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Snowball", "Base damage": 10, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Magic snowball", "Base damage": 10, "Type": "Magic", "Stamina use": 0}
         ]
         }
    ]},
    "cave": {"Max num of enemies": 4, "Min num of enemies": 2, "Enemies": [
        {"Name": "Golemite",
         "Stats": {"Health": 30, "Stamina": 0, "Weakness": ["Magic"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Rock smack", "Base damage": 8, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Rock fall", "Base damage": 8, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Magic rock attack", "Base damage": 8, "Type": "Magic", "Stamina use": 0}
         ]
         },
        {"Name": "Diamond golemite",
         "Stats": {"Health": 40, "Stamina": 0, "Weakness": ["Melee"], "Strong against": ["Magic"]},
         "Moves": [
             {"Move name": "Diamond smack", "Base damage": 10, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Diamond fall", "Base damage": 10, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Magic diamond attack", "Base damage": 10, "Type": "Magic", "Stamina use": 0}
         ]
         }
    ]},
    "mountain": {"Max num of enemies": 4, "Min num of enemies": 2, "Enemies": [
        {"Name": "Cougar",
         "Stats": {"Health": 25, "Stamina": 0, "Weakness": ["Ranged"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Vicious scratch", "Base damage": 10, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Snowball", "Base damage": 10, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Magic snowball", "Base damage": 10, "Type": "Magic", "Stamina use": 0}
         ]
         },
        {"Name": "Snow leapord",
         "Stats": {"Health": 20, "Stamina": 0, "Weakness": ["Melee"], "Strong against": ["Magic"]},
         "Moves": [
             {"Move name": "Vicious scratch", "Base damage": 10, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Snowball", "Base damage": 10, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Magic snowball", "Base damage": 10, "Type": "Magic", "Stamina use": 0}
         ]
         }
    ]},
    "cave final": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "Golem",
         "Stats": {"Health": 70, "Stamina": 0, "Weakness": ["Magic"], "Strong against": ["Melee", "Ranged"]},
         "Moves": [
             {"Move name": "Heavy rock smack", "Base damage": 10, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Heavy rock fall", "Base damage": 10, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Strong magic rock attack", "Base damage": 10, "Type": "Magic", "Stamina use": 0}
         ]
         }
    ]},
    "mountain final": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "Yeti",
         "Stats": {"Health": 60, "Stamina": 0, "Weakness": ["Ranged"], "Strong against": ["Melee","Magic"]},
         "Moves": [
             {"Move name": "Powerful punch", "Base damage": 12, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Big snowball", "Base damage": 12, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Ice ball", "Base damage": 12, "Type": "Magic", "Stamina use": 0}
         ]
         }
    ]},
    "orc road": {"Max num of enemies": 5, "Min num of enemies": 4, "Enemies": [
        {"Name": "Big orc",
         "Stats": {"Health": 30, "Stamina": 14, "Weakness": ["Magic"], "Strong against": ["Melee", "Ranged"]},
         "Moves": [
             {"Move name": "Punch", "Base damage": 4, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Club", "Base damage": 8, "Type": "Melee", "Stamina use": 2},
             {"Move name": "Powerful kick", "Base damage": 8, "Type": "Ranged", "Stamina use": 2}
         ]
         },
        {"Name": "Small orc",
         "Stats": {"Health": 15, "Stamina": 20, "Weakness": ["Magic"], "Strong against": ["Melee", "Ranged"]},
         "Moves": [
             {"Move name": "Punch", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Club", "Base damage": 8, "Type": "Melee", "Stamina use": 2},
             {"Move name": "Kick", "Base damage": 6, "Type": "Ranged", "Stamina use": 2}
         ]
         },
        {"Name": "Orc with a bow",
         "Stats": {"Health": 20, "Stamina": 0, "Weakness": ["Magic"], "Strong against": ["Melee", "Ranged"]},
         "Moves": [
             {"Move name": "Shoot an arrow", "Base damage": 4, "Type": "Ranged", "Stamina use": 0}
         ]
         },
        {"Name": "Orc with a sword",
         "Stats": {"Health": 20, "Stamina": 0, "Weakness": ["Magic"], "Strong against": ["Melee", "Ranged"]},
         "Moves": [
             {"Move name": "Slash", "Base damage": 4, "Type": "Melee", "Stamina use": 0}
         ]
         },
    ]},
    "Area test 1": {"Max num of enemies": 3, "Enemies": [
        {"Name": "test1",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": ["Melee"], "Strong against": ["Ranged"]},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 3, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 6, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 9, "Type": "Melee", "Stamina use": 2}
         ]
         },
        {"Name": "test2",
         "Stats": {"Health": 20, "Stamina": 10, "Weakness": ["Melee"], "Strong against": ["Ranged"]},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 3, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 6, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 9, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]},
    "Area test 2": {"Max num of enemies": 3, "Enemies": [
        {"Name": "test3",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": ["Melee"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 6, "Type": "Melee", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 9, "Type": "Melee", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 12, "Type": "Melee", "Stamina use": 2}
         ]
         },
        {"Name": "test4",
         "Stats": {"Health": 20, "Stamina": 10, "Weakness": ["Ranged"], "Strong against": ["Melee"]},
         "Moves": [
             {"Move name": "Move 1", "Base damage": 6, "Type": "Ranged", "Stamina use": 0},
             {"Move name": "Move 2", "Base damage": 9, "Type": "Ranged", "Stamina use": 1},
             {"Move name": "Move 3", "Base damage": 12, "Type": "Ranged", "Stamina use": 2}
         ]
         },
    ]}
}

# enemy name(same as the possible enemy list) : {"Name" gives the name of drop, cost gives cost}
POSSIBLE_ENEMIES_DROPS = {
    "stubborn rogue sheep": {"Name": "Sheep skin", "Cost": 2},
    "wolf": {"Name": "Wolf skin", "Cost": 5},
    "golemite": {"Name": "Diamond", "Cost": 30},
    "cougar and wolf skin": {"Name": "Cougar and wolf skin skin", "Cost": 30}
                          }

# variables
player_area = "tutorial"

part_one_complete = False

part_two_complete = False

part_three_complete = False

part_four_complete = False

player_money = 0

complete_game = False

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
    elif choice == "restart":
        restart_game()
        return "restart"
    print()

def damage_calculate(thing, move, turn):
    if turn == "Player":
        print("---------------------")
        print("You are attacking", thing["Name"], "with", move["Move name"])
    else:
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("The enemy is attacking with", move["Move name"])

    if turn == "Player":
        if move["Type"] in thing["Stats"]["Weakness"]:
            print("Super effective")
            damage_multiplier = DAMAGE_VALUES["Strong"]
        elif move["Type"] in thing["Stats"]["Strong against"]:
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

    if enter_to_continue() == "restart":
        return "restart"

def show_moves(weapon_info):
    for i in range(0, len(weapon_info)):
        print("Type", i + 1, "for")
        print(weapon_info[i]["Move name"], "| Damage -", weapon_info[i]["Base damage"],
              "| Hit multiple enemies -", weapon_info[i]["Hit multi enemy"], "| Stamina cost -",
              weapon_info[i]["Stamina use"], "| Move type -", weapon_info[i]["Type"])

        if i == len(weapon_info) - 1:
            print()
            print("Type", i + 2, "for")
            print("Rest and gain 5 stamina")

            if len(item_inventory) > 0:
                print()
                print("Type", i + 3, "to")
                print("Use inventory")
            print("---------------")
        print()

# battle function for the game
# takes the player area and gets the corrosponding enemies
def battle(area):
    print()
    print("You are in a battle")

    # tutorial counter - it is for tutorial text just showing up once
    tutorial_counter = 0

    # isolates the player stats list
    player = copy.deepcopy(player_stats)

    # random enemy generation
    num_enemy = random.randint(POSSIBLE_ENEMIES[area]["Min num of enemies"], POSSIBLE_ENEMIES[area]["Max num of enemies"])
    enemies = []

    # adds the enemies to a list and prints out the names
    for i in range(0, num_enemy):
        enemies.append(copy.deepcopy(POSSIBLE_ENEMIES[area]["Enemies"][random.randint(0, len(POSSIBLE_ENEMIES[area]["Enemies"]) - 1)]))
        print("A", enemies[i]["Name"], "appeared")

    if enter_to_continue() == "restart":
        return "restart"

    if player_area == "tutorial":
        print("You take turns attacking each other")
        if enter_to_continue() == "restart":
            return "restart"

    # battle loop
    # starts with players turn and gets input for what to do
    # then checks if player wins or lose
    # then moves onto enemy moves and repeats untill something breaks the loop
    while True:
        # players turn
        if player["Stats"]["Health"] > 0:
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

            if enter_to_continue() == "restart":
                return "restart"

            print("==========")
            print("Your turn")
            print("==========")
            print()

            time.sleep(1)

            print("Your moves: ")
            print("---------------")

            if area == "tutorial" and tutorial_counter == 0:
                print("You will have a choice of options to attack the enemy")
                print("Each move has a type. Depending on the enemy, it may be weak or strong against the type")
                print("If you hit a enemies weakness it will do more damage")
                print("If you hit a enemies strength it will do less damage")
                if enter_to_continue() == "restart":
                    return "restart"
                print("Some moves will be able to hit multiple enemies")
                print("These moves will have [hit multiple enemies - true]")
                if enter_to_continue() == "restart":
                    return "restart"
                print("When you use a move it will deplete your stamina")
                print("Different moves require different amounts stamina to use")
                print("You can rest to gain some stamina back")
                if enter_to_continue() == "restart":
                    return "restart"

            weapon_info = player_equipment["Weapon"]["Info"]

            item_use = 0
            move_selection_max_length = 0
            if len(item_inventory) > 0:
                move_selection_max_length = 2
            else:
                move_selection_max_length = 1

            # choosing what to do
            while True:
                # prints moves
                show_moves(weapon_info)

                possible_move_list = []

                for i in range(0,len(weapon_info)+move_selection_max_length):
                    possible_move_list.append(i+1)
                choose_move = int_error_detection("Choose move to attack the enemy: ", possible_move_list)

                # item inventory menu
                if choose_move == possible_move_list[-1] and move_selection_max_length == 2:

                    possible_item_list = []
                    for i in range(0, len(item_inventory)):
                        print("Type", i + 1, "to use", item_inventory[i]["Name"], "| Healing -",
                              item_inventory[i]["Healing amount"], "health |")
                        print()
                        possible_item_list.append(i+1)

                    last_number = possible_item_list[-1]
                    print("Type", last_number+1, "to go back to move selection")
                    print()

                    possible_item_list.append(last_number+1)

                    player_item_input = int_error_detection("Type here: ", possible_item_list)

                    if player_item_input == "restart":
                        return "restart"

                    last_number = possible_item_list[-1]

                    if player_item_input == last_number:
                        print("Going back to move selection")
                        time.sleep(1.5)
                        show_moves(weapon_info)
                    else:
                        choose_move = "Inventory"
                        player_item_input = player_item_input - 1
                        item_use = item_inventory[player_item_input]
                        item_inventory.pop(player_item_input)
                        print("You are using", item_use["Name"])
                        break

                # resting part
                elif choose_move == (len(possible_move_list)-move_selection_max_length+1):
                    if area == "tutorial":
                        print("You should attack the enemy")
                        time.sleep(1)
                    else:
                        choose_move = "Rest"
                        break
                elif choose_move == "restart":
                    return "restart"

                # move selected
                else:
                    choose_move -= 1
                    choose_move = player_equipment["Weapon"]["Info"][choose_move]
                    break

            # checks what you are doing and does calculation
            if choose_move == "Rest":
                print("You rested")
                print("You gained 5 stamina")
                player["Stats"]["Stamina"] += 5
                print("You are at", player["Stats"]["Stamina"], "stamina")
                print()
            elif choose_move == "Inventory":
                print("You ate", item_use["Name"])
                print("It healed", item_use["Healing amount"], "health")
                player["Stats"]["Health"] += item_use["Healing amount"]
                print("You are now at", player["Stats"]["Health"], "health")
                if enter_to_continue() == "restart":
                    return "restart"
            else:
                target = []

                # enemy selection
                if choose_move["Hit multi enemy"] == False and len(enemies) > 1:

                    possible_enemy_select = []

                    for i in range(0, len(enemies)):
                        print("Type", i + 1, "to attack", enemies[i]["Name"])
                        possible_enemy_select.append(i+1)

                    choose_target = int_error_detection("Choose enemy: ", possible_enemy_select)

                    if choose_target == "restart":
                        return "restart"
                    else:
                        target.append([enemies[choose_target - 1]])

                elif len(enemies) == 1:
                    target.append([enemies[0]])

                elif choose_move["Hit multi enemy"] == True and len(enemies) >= 2:
                    for i in range(0, len(enemies)):
                        target.append([enemies[i]])

                print()
                print(choose_move["Move name"], "used", choose_move["Stamina use"], "stamina")
                player["Stats"]["Stamina"] = player["Stats"]["Stamina"] - choose_move["Stamina use"]
                print("You are at", player["Stats"]["Stamina"], "stamina")

                if enter_to_continue() == "restart":
                    return "restart"

                # damage calc
                # also removes enemies from list if dead
                for i in range(0, len(target)):
                    damage_calculate(target[i][0], choose_move, "Player")
                    # after damage calculation it checks if it is dead and if it is it will remove it from the enemies list
                    if target[i][0]["Stats"]["Health"] <= 0:
                        enemies.remove(target[i][0])

        # check if player is dead and if so breaks the loop
        elif player["Stats"]["Health"] <= 0:
            print("You lose")
            print("Ganbalf will now time travel you back to the day before")
            if enter_to_continue() == "restart":
                return "restart"
            return "Lost"

        # checks if you have killed all the enemies
        if len(enemies) == 0:
            print("You won the battle")
            time.sleep(1)
            break

        if area == "tutorial" and tutorial_counter == 0:
            print("It is now time for the enemy to attack")
            time.sleep(1.5)

        print("~~~~~~~~~~~~")
        print("Enemies turn")
        print("~~~~~~~~~~~~")
        time.sleep(1.5)

        # enemy ai
        for i in range(0, len(enemies)):
            if enter_to_continue() == "restart":
                return "restart"

            # enemy ai for 1 enemy
            # check if enemy is alive
            enemy = enemies[i]
            if enemy["Stats"]["Health"] > 0:

                # chooses a random move
                # if the random move stamina cost to high than it defaults to the basic 0 stamina cost move
                # this makes it easier to play against i.e less damaging attacks more weaker attacks
                random_move_num = random.randint(0, len(enemy["Moves"]) - 1)

                # check stamina and choose a move
                if enemy["Moves"][random_move_num]["Stamina use"] <= enemy["Stats"]["Stamina"]:
                    enemy_move = enemy["Moves"][random_move_num]
                else:
                    enemy_move = enemy["Moves"][0]  # move 1 or 0 stamina use is always at 0

                enemy["Stats"]["Stamina"] = enemy["Stats"]["Stamina"] - enemy_move["Stamina use"]

                damage_calculate(player, enemy_move, "Enemy")

        # changes the tutorial counter so the tutorial doesn't spam in your face
        tutorial_counter += 1

# answers is a list
# basic error detection for small inputs
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
            elif player_input.lower() == "restart":
                restart_game()
                return "restart"
            else:
                print("Not an integer")

def enter_shop(shop_area):
    global player_money

    print("You entered", shop_area)

    time.sleep(1)

    while True:

        # choose what to do
        print("Type 1 to equip armour and weapons")
        print("Type 2 to purchase armour and weapons")
        print("Type 3 to sell armour and weapons")
        print("Type 4 to purchase items")
        print("Type 5 to sell items")
        print("Type 6 to leave the shop")
        player_input = int_error_detection(": ", [1,2,3,4,5,6])

        if player_input == "restart":
            return "restart"

        # equiping armour/weapons
        elif player_input == 1:
            if len(player_spare_equipment["Armour"]) > 0 or len(player_spare_equipment["Weapons"]) > 0:
                print("----------------------------------------")
                print("Current equipment")
                print()
                print("Weapon:", player_equipment["Weapon"]["Name"])
                print_weapon_stats(player_equipment["Weapon"])
                print("Armour:", player_equipment["Armour"]["Name"])
                print_armour_stats(player_equipment["Armour"])
                print("----------------------------------------")
                print("Spare equipment")
                print()

                if len(player_spare_equipment["Weapons"]) > 0:
                    for i in range(0,len(player_spare_equipment["Weapons"])):
                        print(player_spare_equipment["Weapons"][i]["Name"], "(Weapon)")
                if len(player_spare_equipment["Armour"]) > 0:
                    for i in range(0,len(player_spare_equipment["Armour"])):
                        print(player_spare_equipment["Armour"][i]["Name"], "(Armour)")
                print("----------------------------------------")

                # need to do equipment code here


                while True:
                    possible_equips = []

                    for i in range(0, len(player_spare_equipment["Weapons"])):
                        print("Type", i + 1, "to equip", player_spare_equipment["Weapons"][i]["Name"])
                        possible_equips.append((i + 1))

                    try:
                        last_number = possible_equips[-1]
                    except IndexError:
                        last_number = 0

                    for i in range(0, len(player_spare_equipment["Armour"])):
                        print("Type", last_number + i + 1, "to equip", player_spare_equipment["Armour"][i]["Name"])
                        possible_equips.append((last_number + i + 1))

                    print("Type", possible_equips[-1]+1, "to not equip anything and leave this menu")
                    possible_equips.append((possible_equips[-1] + 1))

                    last_number = possible_equips[-1]


                    one_time_input = int_error_detection(": ", possible_equips)

                    if one_time_input == "restart":
                        return "restart"

                    elif one_time_input == last_number:
                        print("You did not equip anything")
                        time.sleep(1)
                        break

                    elif one_time_input <= len(player_spare_equipment["Weapons"]):
                        # index the variable
                        one_time_input -= 1

                        print("You are equiping", player_spare_equipment["Weapons"][one_time_input]["Name"])
                        time.sleep(1)
                        print("You put", player_equipment["Weapon"]["Name"], "into your spare equipment")
                        time.sleep(1)

                        player_spare_equipment["Weapons"].append(player_equipment["Weapon"])
                        player_equipment["Weapon"] = player_spare_equipment["Weapons"][one_time_input]
                        player_spare_equipment["Weapons"].pop(one_time_input)

                    elif one_time_input > len(player_spare_equipment["Weapons"]):
                        # index the variable
                        one_time_input = one_time_input - len(player_spare_equipment["Weapons"]) - 1

                        print("You are equiping", player_spare_equipment["Armour"][one_time_input]["Name"])
                        time.sleep(1)
                        print("You put", player_equipment["Armour"]["Name"], "into your spare equipment")
                        time.sleep(1)

                        player_spare_equipment["Armour"].append(player_equipment["Armour"])
                        player_equipment["Armour"] = player_spare_equipment["Armour"][one_time_input]
                        player_spare_equipment["Armour"].pop(one_time_input)
            else:
                print("You do not have any spare equipment")
                time.sleep(1)

        # buying armour / weapons
        if player_input == 2:

            # prints out information
            print("========================================")
            print("Weapons for sale")

            for i in range(0,len(POSSIBLE_WEAPONS[shop_area])):
                print()
                print(POSSIBLE_WEAPONS[shop_area][i]["Name"], "costs", POSSIBLE_WEAPONS[shop_area][i]["Cost"], "dollars | info below")
                print_weapon_stats(POSSIBLE_WEAPONS[shop_area][i])
            print("========================================")
            print("Armour for sale")

            for i in range(0, len(POSSIBLE_ARMOUR[shop_area])):
                print()
                print(POSSIBLE_ARMOUR[shop_area][i]["Name"], "costs", POSSIBLE_ARMOUR[shop_area][i]["Cost"], "dollars")
                print_armour_stats(POSSIBLE_ARMOUR[shop_area][i])
            print("========================================")

            # purchasing code
            while True:
                print()
                possible_purchases = []
                print("Scroll up to view all weapons and armour")

                for i in range(0, len(POSSIBLE_WEAPONS[shop_area])):
                    print("Type", i + 1, "to purchase", POSSIBLE_WEAPONS[shop_area][i]["Name"])
                    possible_purchases.append((i + 1))

                try:
                    last_number = possible_purchases[-1]
                except IndexError:
                    last_number = 0

                for i in range(0, len(POSSIBLE_ARMOUR[shop_area])):
                    print("Type", last_number + i + 1, "to purchase", POSSIBLE_ARMOUR[shop_area][i]["Name"])
                    possible_purchases.append(last_number + (i + 1))

                possible_purchases.append(possible_purchases[-1] + 1)
                print("Type", possible_purchases[-1], "to not buy anything")

                last_number = possible_purchases[-1]

                one_time_input = int_error_detection(": ", possible_purchases)

                if one_time_input == "restart":
                    return "restart"

                # one_time_input is NOT IN INDEX FORM

                elif one_time_input == last_number:
                    print("You did not buy anything")
                    time.sleep(1)
                    break
                elif one_time_input <= len(POSSIBLE_WEAPONS[shop_area]):
                    # Turns the variable into an index form so lists can use it
                    one_time_input -= 1
                    if POSSIBLE_WEAPONS[shop_area][one_time_input]["Cost"] <= player_money:
                        print("You spent", POSSIBLE_WEAPONS[shop_area][one_time_input]["Cost"], "dollars")
                        player_money -= POSSIBLE_WEAPONS[shop_area][one_time_input]["Cost"]
                        print("You have", player_money, "dollars")
                        time.sleep(1)

                        print("You purchased", POSSIBLE_WEAPONS[shop_area][one_time_input]["Name"])
                        player_spare_equipment["Weapons"].append(POSSIBLE_WEAPONS[shop_area][one_time_input])
                        print("You put your weapon into your spare equipment")
                        print("To equip it go to the equipment page in the shop")
                        time.sleep(2)
                    else:
                        print("You do not have enough money to purchase this armour")
                        time.sleep(1)
                        print("You have", player_money, "dollars")
                        print("You need", POSSIBLE_WEAPONS[shop_area][one_time_input]["Cost"], "dollars to purchase", POSSIBLE_WEAPONS[shop_area][one_time_input]["Name"])
                elif one_time_input > len(POSSIBLE_WEAPONS[shop_area]):
                    # this gets the number to index form
                    one_time_input = one_time_input - len(POSSIBLE_WEAPONS[shop_area]) - 1
                    if POSSIBLE_ARMOUR[shop_area][one_time_input]["Cost"] <= player_money:
                        print("You spent", POSSIBLE_ARMOUR[shop_area][one_time_input]["Cost"], "dollars")
                        player_money -= POSSIBLE_ARMOUR[shop_area][one_time_input]["Cost"]
                        print("You have", player_money, "dollars")
                        time.sleep(1)

                        player_spare_equipment["Armour"].append(POSSIBLE_ARMOUR[shop_area][one_time_input])
                        print("You purchased", POSSIBLE_ARMOUR[shop_area][one_time_input]["Name"])
                        print("You put your armour into your spare equipment")
                        print("To equip it go to the equipment page in the shop")
                        time.sleep(2)
                    else:
                        print("You do not have enough money to purchase this armour")
                        time.sleep(1)
                        print("You have", player_money, "dollars")
                        print("You need", POSSIBLE_ARMOUR[shop_area][one_time_input]["Cost"], "dollars to purchase", POSSIBLE_ARMOUR[shop_area][one_time_input]["Name"])

        # selling armour / weapons
        if player_input == 3:
            if len(player_spare_equipment["Armour"]) <= 0 and len(player_spare_equipment["Weapons"]) <= 0:
                print("You do not have any equipment to sell")
                time.sleep(1)
            else:
                print("You can sell your spare equipments")
                time.sleep(1)

                while True:

                    if len(player_spare_equipment["Armour"]) <= 0 and len(player_spare_equipment["Weapons"]) <= 0:
                        print("You do not have any equipment to sell")
                        time.sleep(1)
                        break

                    if len(player_spare_equipment["Weapons"]) > 0:
                        for i in range(0, len(player_spare_equipment["Weapons"])):
                            print(player_spare_equipment["Weapons"][i]["Name"], "(Weapon)", "| sells for -", player_spare_equipment["Weapons"][i]["Cost"], "dollars")
                    if len(player_spare_equipment["Armour"]) > 0:
                        for i in range(0, len(player_spare_equipment["Armour"])):
                            print(player_spare_equipment["Armour"][i]["Name"], "(Armour)", "| sells for -", player_spare_equipment["Armour"][i]["Cost"], "dollars")

                    possible_sells = []

                    for i in range(0, len(player_spare_equipment["Weapons"])):
                        print("Type", i + 1, "to sell", player_spare_equipment["Weapons"][i]["Name"])
                        possible_sells.append((i + 1))

                    try:
                        last_number = possible_sells[-1]
                    except IndexError:
                        last_number = 0

                    for i in range(0, len(player_spare_equipment["Armour"])):
                        print("Type", last_number + i + 1, "to sell", player_spare_equipment["Armour"][i]["Name"])
                        possible_sells.append((last_number + i + 1))

                    print("Type", possible_sells[-1] + 1, "to not sell anything and leave this menu")
                    possible_sells.append((possible_sells[-1] + 1))

                    last_number = possible_sells[-1]

                    one_time_input = int_error_detection(": ", possible_sells)

                    if one_time_input == "restart":
                        return "restart"

                    elif one_time_input == last_number:
                        print("You did not sell anything")
                        time.sleep(1)
                        break

                    elif one_time_input <= len(player_spare_equipment["Weapons"]):
                        # index the variable
                        one_time_input -= 1

                        print("You are selling", player_spare_equipment["Weapons"][one_time_input]["Name"])
                        time.sleep(1)
                        print("You sold", player_spare_equipment["Weapons"][one_time_input]["Name"], "you got", player_spare_equipment["Weapons"][one_time_input]["Cost"], "dollars")
                        time.sleep(1)

                        player_money += player_spare_equipment["Weapons"][one_time_input]["Cost"]
                        player_spare_equipment["Weapons"].pop(one_time_input)

                        print("You now have", player_money, "dollars")
                        time.sleep(1)

                    elif one_time_input > len(player_spare_equipment["Weapons"]):
                        # index the variable
                        one_time_input = one_time_input - len(player_spare_equipment["Weapons"]) - 1

                        print("You are selling", player_spare_equipment["Armour"][one_time_input]["Name"])
                        time.sleep(1)
                        print("You sold", player_spare_equipment["Armour"][one_time_input]["Name"], "you got", player_spare_equipment["Armour"][one_time_input]["Cost"], "dollars")
                        time.sleep(1)

                        player_money += player_spare_equipment["Armour"][one_time_input]["Cost"]
                        player_spare_equipment["Armour"].pop(one_time_input)

                        print("You now have", player_money, "dollars")
                        time.sleep(1)

        # buying items
        if player_input == 4:
            while True:
                possible_items = []

                print("Items")
                for i in range(0, len(POSSIBLE_ITEMS[shop_area])):
                    print("Type", i+1, "to buy", POSSIBLE_ITEMS[shop_area][i]["Name"], "it costs", POSSIBLE_ITEMS[shop_area][i]["Cost"], "dollars")
                    possible_items.append(i+1)

                last_number = possible_items[-1]
                print("Type", last_number+1, "to leave this menu")
                possible_items.append(last_number+1)

                one_time_input = int_error_detection(": ", possible_items)

                if one_time_input == "restart":
                    return "restart"

                one_time_input -= 1
                if one_time_input == last_number:
                    print("You did not buy anything")
                    time.sleep(1)
                    break

                elif POSSIBLE_ITEMS[shop_area][one_time_input]["Cost"] <= player_money:
                    print("You bought", POSSIBLE_ITEMS[shop_area][one_time_input]["Name"])
                    print("It cost", POSSIBLE_ITEMS[shop_area][one_time_input]["Cost"], "dollars")

                    item_inventory.append(POSSIBLE_ITEMS[shop_area][one_time_input])

                    player_money -= POSSIBLE_ITEMS[shop_area][one_time_input]["Cost"]

                    print("You now have", player_money, "dollars")

                else:
                    print("You do not have enough money to purchase", POSSIBLE_ITEMS[shop_area][one_time_input]["Name"])
                    time.sleep(1)
                    print("You have", player_money, "dollars")
                    time.sleep(1)
                    print("You need", POSSIBLE_ITEMS[shop_area][one_time_input]["Cost"], "dollars to purchase this")
                    time.sleep(1)

        # selling items
        if player_input == 5:
            if len(player_drop_inventory) > 0 or len(item_inventory) > 0:
                while True:

                    if len(player_drop_inventory) == 0 and len(item_inventory) == 0:
                        print("You do not have any items to sell")
                        time.sleep(1)
                        break

                    possible_item_sell = []
                    for i in range(0, len(item_inventory)):
                        print("Type", i+ 1, item_inventory[i]["Name"], "sells for", item_inventory[i]["Cost"], "dollars")
                        possible_item_sell.append(i+1)

                    try:
                        last_number = possible_item_sell[-1]
                    except IndexError:
                        last_number = 0

                    for i in range(0, len(player_drop_inventory)):
                        print("Type", i+1, player_drop_inventory[i]["Name"], "sells for", player_drop_inventory[i]["Cost"], "dollars")
                        possible_item_sell.append(i+1)

                    print("Type", possible_item_sell[-1] + 1, "to not sell anything and leave this menu")
                    possible_item_sell.append((possible_item_sell[-1] + 1))

                    last_number = possible_item_sell[-1]

                    one_time_input = int_error_detection(": ", possible_item_sell)

                    if one_time_input == "restart":
                        return "restart"

                    elif one_time_input == last_number:
                        print("You did not sell anything")
                        time.sleep(1)
                        break

                    elif one_time_input <= len(item_inventory):
                        # puts variable into index form
                        one_time_input -= 1

                        print("You sold", item_inventory[one_time_input]["Name"], "for", item_inventory[one_time_input]["Cost"], "dollars")
                        player_money += item_inventory[one_time_input]["Cost"]
                        item_inventory.pop(one_time_input)

                        print("You now have", player_money, "dollars")

                    elif one_time_input > len(item_inventory):
                        # puts variable into index form
                        one_time_input = one_time_input - len(item_inventory) - 1
                        print("You sold", player_drop_inventory[one_time_input]["Name"], "for", player_drop_inventory[one_time_input]["Cost"], "dollars")

                        player_money += player_drop_inventory[one_time_input]["Cost"]
                        player_drop_inventory.pop(one_time_input)

                        print("You now have", player_money, "dollars")
            else:
                print("You do not have any items to sell")
                time.sleep(1)

        # leaving the shop
        if player_input == 6:
            print("You are leaving the shop")
            time.sleep(1)
            break
        print()

def print_weapon_stats(weapon):
    for y in range(0, len(weapon["Info"])):
        weapon_info = weapon["Info"][y]
        print(weapon_info["Move name"], "| Damage -", weapon_info["Base damage"],
              "| Hit multiple enemies -", weapon_info["Hit multi enemy"], "| Stamina cost -",
              weapon_info["Stamina use"], "| Move type -", weapon_info["Type"])
    print()

def print_armour_stats(armour):
    print("Weakness: ", end='')
    for i in range(0,len(armour["Weakness"])):
        print(armour["Weakness"][i], "", end='')
    print()
    print("Strong against: ", end='')
    for i in range(0,len(armour["Strong against"])):
        print(armour["Strong against"][i], "", end='')
    print()

def part_one():
    global player_area
    global part_one_complete
    global player_money

    print("You are currently at Hobbitown.")
    print("To reach Mount Dooom you must follow the main road.")

    time.sleep(2)

    print("As you travel down the main road you notice something.")
    time.sleep(1.5)
    print("A stubborn rogue sheep blocks the way.")

    time.sleep(1.5)

    print("Type 1 to fight the sheep")
    print("Type 2 to run around the sheep")
    one_use_answer = int_error_detection(": ", [1, 2])

    if one_use_answer == "restart":
        return "restart"
    elif one_use_answer == 1:
        print("You chose to fight the sheep.")
    elif one_use_answer == 2:
        print("You tried to run around but the sheep attacked you.")

    time.sleep(1.5)

    result = battle(player_area)
    if result == "Lost":
        return
    if result == "restart":
        return "restart"

    player_drop_inventory.append(POSSIBLE_ENEMIES_DROPS["stubborn rogue sheep"])
    item_inventory.append(POSSIBLE_ITEMS["Shop 1"][0])
    print("You got", POSSIBLE_ENEMIES_DROPS["stubborn rogue sheep"]["Name"])
    time.sleep(1.5)
    print("You also got", POSSIBLE_ITEMS["Shop 1"][0]["Name"], "from the stubborn rogue sheep's mouth")
    time.sleep(1.5)
    print("When you defeat enemies you can gain items.")
    print("Some items, like the sheep skin, can only be sold.")
    print("Items, like an apple, can be used in battle to heal.")
    time.sleep(2.5)
    print("All items can be sold to a shopkeeper for money.")

    if enter_to_continue() == "restart":
        return "restart"

    print("You continue along the road.")
    time.sleep(1.5)
    print("There seem to be a group of goblins blocking the way.")
    time.sleep(1.5)

    print("What do you do?")
    print("Type 1 - follow the main road and face the group of goblins.")
    print("type 2 - go around them through the forest.")

    one_use_answer = int_error_detection(": ", [1, 2])

    print()

    if one_use_answer == "restart":
        return "restart"
    elif one_use_answer == 1:
        print("You chose to follow the main road.")
        time.sleep(1.5)
        print("The goblins are threatened by your presence and decid to attack you.")
        player_area = "main road 1"
    elif one_use_answer == 2:
        print("You decide to go through the forest.")
        time.sleep(1.5)
        print("A pack of wolves surround you.")
        player_area = "forest 1"

    time.sleep(1.5)
    result = battle(player_area)
    if result == "Lost":
        return
    if result == "restart":
        return "restart"

    if player_area == "forest 1":
        player_drop_inventory.append(POSSIBLE_ENEMIES_DROPS["wolf"])
        print("You got wolf skin from defeating the pack of wolves.")
        time.sleep(1.5)
        print("You decide to go back on the road.")
        player_area = "main road"

        if enter_to_continue() == "restart":
            return "restart"
        print("You continue to travel down the road.")
        time.sleep(1.5)
        print("You see a goblin gang coming towards you.")

    elif player_area == "main road 1":
        player_money += 5
        print("You got 5 dollars from defeating the goblins.")
        time.sleep(1.5)
        print("You decide to continue down the main road.")
        player_area = "main road"
        if enter_to_continue() == "restart":
            return "restart"
        print("The previous group of goblins have come back with reinforcements.")

    time.sleep(1.5)
    print("You are attacked by a goblin gang.")
    time.sleep(1.5)

    result = battle(player_area)
    if result == "Lost":
        return
    if result == "restart":
        return "restart"
    player_money += 7
    print("You got 7 dollars from defeating the goblin gang.")

    player_area = "main road final"

    print("You are coming up to the first town in your journey.")
    time.sleep(1.5)
    print("However, there seems to be a goblin giant blocking the entrance.")
    time.sleep(1.5)
    print("There is no way around.")


    while True:
        print("Are you prepared to fight it?")
        print("Type 1 - yes")
        print("Type 2 - no")
        one_time_input = int_error_detection(": ", [1, 2])

        if one_time_input == "restart":
            return "restart"

        elif one_time_input == 2:
            print("You wait around, expecting the goblin giant to move.")
            time.sleep(2)
            print("The goblin giant doesn't move.")
            time.sleep(2)
        elif one_time_input == 1:
            break

    result = battle(player_area)
    if result == "Lost":
        return
    if result == "restart":
        return "restart"

    print("You defeat the goblin giant.")
    player_money += 10
    print("The goblin giant drop 10 dollars.")

    if enter_to_continue() == "restart":
        return "restart"

    print("You arrive at Brie Town.")
    print("There seems to be a shop that you can stock up on equipment.")
    if enter_to_continue() == "restart":
        return "restart"

    print("Type 1 - go the shop")
    print("Type 2 - continue the quest")
    one_use_answer = int_error_detection(": ", [1, 2])

    if one_use_answer == "restart":
        return "restart"
    elif one_use_answer == 1:
        enter_shop("Shop 1")

    # end of part one
    part_one_complete = True

def part_two():
    global player_area
    global player_money
    global part_two_complete

    print("You follow the main road which takes you up a mountainside.")
    time.sleep(1.5)

    print("You stop at a junction")
    time.sleep(1.5)

    print("There are two signs. The left sign says caves. The other says mountains.")
    time.sleep(1.5)

    print("Type 1 - go left to the caves")
    print("Type 2 - go right to the mountains")

    one_use_answer = int_error_detection(": ", [1, 2])
    if one_use_answer == "restart":
        return "restart"

    # caves path
    elif one_use_answer == 1:
        print("You go down the steep path way leading to the caves.")
        time.sleep(1.5)
        print("As you enter the cave entrance, you are attacked by a little golemite.")
        time.sleep(1.5)
        player_area = "caves 1"
        result = battle(player_area)
        if result == "Lost":
            return
        if result == "restart":
            return "restart"

        player_area = "caves"
        for i in range(0,2):
            print("You continue following the path")
            time.sleep(1.5)
            result = battle(player_area)
            if result == "Lost":
                return
            if result == "restart":
                return "restart"
            player_drop_inventory.append(POSSIBLE_ENEMIES_DROPS["golemite"])
            print("You got a diamond from the golemite.")
            time.sleep(1.5)

        print("You continue to follow the path.")
        time.sleep(1.5)
        print("As you reach the end of the path, a golem attacks you.")
        time.sleep(1.5)
        player_area = "caves final"
        result = battle(player_area)
        if result == "Lost":
            return
        if result == "restart":
            return "restart"
        print("You got the legendary rock sword.")
        time.sleep(1)
        print("You put it into your spare equipment.")
        player_spare_equipment.append(POSSIBLE_WEAPONS["part 2 encouter"][0])

    # mountain path
    elif one_use_answer == 2:
        print("You go up a steep path way leading to the mountain top.")
        time.sleep(1.5)
        print("As you walk the treacherous path, you are attacked by a cougar.")
        time.sleep(1.5)
        player_area = "mountain 1"

        result = battle(player_area)
        if result == "Lost":
            return
        if result == "restart":
            return "restart"

        player_area = "mountain"
        for i in range(0, 2):
            print("You continue to follow the path.")
            time.sleep(1.5)
            result = battle(player_area)
            if result == "Lost":
                return
            if result == "restart":
                return "restart"
            player_drop_inventory.append(POSSIBLE_ENEMIES_DROPS["cougar and wolf skin"])
            print("You got a cougar and wolf skin from the golemite.")

        print("You continue along the path.")
        time.sleep(1.5)
        print("As you reach the end of the path, a yeti attacks you.")
        time.sleep(1.5)
        player_area = "mountain final"
        result = battle(player_area)
        if result == "Lost":
            return
        if result == "restart":
            return "restart"
        print("You got the legendary snow sword.")
        time.sleep(1)
        print("You put it into your spare equipment.")
        player_spare_equipment.append(POSSIBLE_WEAPONS["part 2 encouter"][1])

    time.sleep(1.5)
    print("You continue along the path")
    time.sleep(1.5)
    print("You reach the next _______ town")
    time.sleep(1.5)
    print("There also seems to be a shop here too")

    if enter_to_continue() == "restart":
        return "restart"

    print("Type 1 - go the shop")
    print("Type 2 - continue the quest")
    one_use_answer = int_error_detection(": ", [1, 2])

    if one_use_answer == "restart":
        return "restart"
    elif one_use_answer == 1:
        enter_shop("Shop 2")

    part_two_complete = True

def main_code():
    global player_stats

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
            elif start_choice == "restart":
                restart_game()
                return "restart"
            else:
                print("Not a valid string")
        except ValueError:
            print("Not a valid input")

    # Code for quiting the game. Checks if the answer is no then runs the quit function
    if start_choice == "no":
        quit_game()

    print("Welcome")

    time.sleep(1)

    print()
    print("Infomation")
    print("-------------------------------")
    print("You can type quit to quit or restart to restart at any of the inputs.")
    print("-------------------------------")
    print()

    time.sleep(1)

    print(
        "There will be tutorials on how to play throughout the game but do you want a more detailed guide on the mechanics that are not covered by the tutorial?")
    print("Type 1 - yes")
    print("Type 2 - no")

    one_time_input = int_error_detection(":", [1, 2])
    if one_time_input == "restart":
        return "restart"

    elif one_time_input == 1:
        print("The games combat is turn based.")
        if enter_to_continue() == "restart":
            return "restart"
        print("If you die you, will be sent back to the last place you slept/rested in.")
        if enter_to_continue() == "restart":
            return "restart"
        print("You will choose a character and each character will have 5 stats.")
        time.sleep(3)
        print("Health shows your health status. If you are at 0 or below, you will die and lose the game.")
        print("When you heal, can go over your max health.")
        print()
        print("Base damage is how much damage will be dealt.")
        print()
        print("Defense is a stat that reduces the incoming damage.")
        print()
        print("Strength is a stat that will increase the damage outgoing.")
        print()
        print("Stamina is a 'currency' for moves.")
        print("Depending on the move it will cost your character stamina.")
        print("If you are out on stamina, you will not be able to pick that move.")

    if enter_to_continue() == "restart":
        return "restart"

    print("Ganbalf has sent you on a quest to destroy a ring and save Centre Earth from Zauron.")
    print("You must venture to Mount Dooom where you will destroy the ring.")

    if enter_to_continue() == "restart":
        return "restart"

    print("-------------------------------")
    print("Choose your character")
    print("-------------------------------")

    time.sleep(1)

    # for loop that prints out the possible classes and another for loop for lists out want input for which class to choose
    for i in range(len(POSSIBLE_CLASSES)):
        print("Character", i + 1, ":", POSSIBLE_CLASSES[i]["Name"])
        print("Stats: ")
        print("| Health:", POSSIBLE_CLASSES[i]["Stats"]["Health"], "| Base damage:",
              POSSIBLE_CLASSES[i]["Stats"]["Bonus damage"],
              "| Defense:", POSSIBLE_CLASSES[i]["Stats"]["Defense"], "| Strength:",
              POSSIBLE_CLASSES[i]["Stats"]["Strength"],
              "| Stamina:", POSSIBLE_CLASSES[i]["Stats"]["Stamina"])
        print()

    print()

    one_time_possible_list = []

    for i in range(len(POSSIBLE_CLASSES)):
        print("Type", i + 1, "for", POSSIBLE_CLASSES[i]["Name"])
        one_time_possible_list.append(i + 1)

    # another while loop with try and except. Asks for a which class using 1,2,3 etc.
    # If input str or bool will run try and except and ask again. If number is too big or too small will ask fo input again.
    print()

    print("Choose a character", end=' ')
    one_time_input = int_error_detection(":", one_time_possible_list)

    if one_time_input == "restart":
        return "restart"

    one_time_input -= 1
    print("You chose: ", POSSIBLE_CLASSES[one_time_input]["Name"])
    player_stats = POSSIBLE_CLASSES[one_time_input]

    if enter_to_continue() == "restart":
        return "restart"

    print("-------------------------------")
    print("Ganbalf has also supplied you a choice of weapons.")
    print("Choose one")
    print("-------------------------------")

    time.sleep(1)

    one_time_possible_list = []

    for x in range(0, len(POSSIBLE_WEAPONS["tutorial"])):
        print("Armour", x + 1, ":", POSSIBLE_WEAPONS["tutorial"][x]["Name"])
        print("Info: ")
        print_weapon_stats(POSSIBLE_WEAPONS["tutorial"][x])

    for i in range(0, len(POSSIBLE_WEAPONS[player_area])):
        print("Type", i + 1, "for", POSSIBLE_WEAPONS[player_area][i]["Name"])
        one_time_possible_list.append(i + 1)

    print("Choose a weapon", end=' ')
    one_time_input = int_error_detection(":", one_time_possible_list)

    if one_time_input == "restart":
        return "restart"

    one_time_input -= 1
    print("You chose: ", POSSIBLE_WEAPONS[player_area][one_time_input]["Name"])
    player_equipment["Weapon"] = POSSIBLE_WEAPONS[player_area][one_time_input]

    if enter_to_continue() == "restart":
        return "restart"

    while part_one_complete == False:
        if part_one() == "restart":
            return "restart"

    print("It is getting late. You decide to go the Galloping Horse Inn to rest.")
    time.sleep(2)

    print("In the morning you leave the town and continue on the main road.")
    time.sleep(1.5)

    while part_two_complete == False:
        if part_two() == "restart":
            return "restart"

    print("It is getting late. You decide to go the _____ to rest.")
    time.sleep(2)

    print("In the morning you leave the town and continue on the main road.")
    time.sleep(1.5)

    print("end so far")


    while part_four_complete == False:
        pass
        # do the same with the part two etc here

    # after all parts complete it will return main code to "complete game"

def restart_game():
    global player_stats
    global player_equipment
    global player_spare_equipment
    global player_drop_inventory
    global player_equipment
    global item_inventory
    global player_area
    global part_one_complete
    global part_two_complete
    global complete_game
    global player_money
    global part_three_complete
    global part_four_complete

    player_stats = {}
    player_equipment = {"Weapon": {},"Armour": {"Name": "Basic Armour","Weakness": ["None"],"Strong against": ["None"],"Cost": 5}}
    player_spare_equipment = {"Weapons": [],"Armour": []}
    player_drop_inventory = []
    item_inventory = []
    player_area = "tutorial"
    part_one_complete = False
    part_two_complete = False
    part_three_complete = False
    part_four_complete = False
    player_money = 0
    complete_game = False

# ----------------------- Main code -----------------------

#player_money = 99999
#player_stats = POSSIBLE_CLASSES[0]
#player_equipment["Weapon"] = POSSIBLE_WEAPONS["tutorial"][0]
#player_spare_equipment["Weapons"].append(POSSIBLE_WEAPONS["Shop 1"][0])
#player_spare_equipment["Armour"].append(POSSIBLE_ARMOUR["Shop 1"][0])
#item_inventory.append(POSSIBLE_ITEMS["Shop 1"][0])
#enter_shop("Shop 2")
#battle("forest 1")

while True:
    check_if_complete = main_code()

    if check_if_complete == "restart":
        print("restarting")
        time.sleep(2)
    elif check_if_complete == "complete game":
        print("You completed the game")
        break

