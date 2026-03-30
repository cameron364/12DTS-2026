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
                {"Move name": "Slash", "Base damage": 3, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Jab", "Base damage": 4, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2}]},
        {"Name": "Starter Wand", "Cost": 5,
            "Info": [
                {"Move name": "Zap", "Base damage": 6, "Hit multi enemy": False, "Type": "Magic", "Stamina use": 2},
                {"Move name": "Fireball", "Base damage": 5, "Hit multi enemy": True, "Type": "Magic", "Stamina use": 3},
                {"Move name": "Poke", "Base damage": 2, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1}]},
        {"Name": "Starter Axe", "Cost": 5,
            "Info": [
                {"Move name": "Cut", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Throw axe", "Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 2}]}
    ],
    "Shop 1": [
        {"Name": "Sword", "Cost": 10,
            "Info": [
                {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 1},
                {"Move name": "Move 2", "Base damage": 2, "Hit multi enemy": True, "Type": "Melee", "Stamina use": 2},
                {"Move name": "Move 3", "Base damage": 7, "Hit multi enemy": False, "Type": "Melee", "Stamina use": 3}
            ]},
        {"Name": "Bow", "Cost": 10,
            "Info": [
                {"Move name": "Move 1", "Base damage": 5, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 1},
                {"Move name": "Move 2", "Base damage": 2, "Hit multi enemy": True, "Type": "Ranged", "Stamina use": 2},
                {"Move name": "Move 3", "Base damage": 7, "Hit multi enemy": False, "Type": "Ranged", "Stamina use": 3}]}
    ]
}

POSSIBLE_ARMOUR = {
    "Shop 1": [
    {
        "Name": "Chainmail",
        "Cost": 5,
        "Weakness": ["None"],
        "Strong against": ["Melee","Ranged"]
    },
    {
        "Name": "Knights Armour",
        "Cost": 5,
        "Weakness": ["Magic"],
        "Strong against": ["Melee","Ranged"]
    }
]}

POSSIBLE_ENEMIES = {
    "tutorial": {"Max num of enemies": 1, "Min num of enemies": 1, "Enemies": [
        {"Name": "stubborn rogue sheep",
         "Stats": {"Health": 10, "Stamina": 5, "Weakness": ["Melee","Ranged","Magic"], "Strong against": ["None"]},
         "Moves": [
             {"Move name": "Bash", "Base damage": 2, "Type": "Melee", "Stamina use": 0},
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
    "wolf": {"Name": "Wolf skin", "Cost": 5}
                          }

# variables
player_area = "tutorial"

player_money = 99999

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

    enter_to_continue()

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

def battle(area):
    print()
    print("You are in a battle")

    # isolates the player stats list
    player = copy.deepcopy(player_stats)

    # random enemy generation
    num_enemy = random.randint(POSSIBLE_ENEMIES[area]["Min num of enemies"], POSSIBLE_ENEMIES[area]["Max num of enemies"])
    enemies = []

    # adds the enemies to a list and prints out the names
    for i in range(0, num_enemy):
        enemies.append(copy.deepcopy(POSSIBLE_ENEMIES[area]["Enemies"][random.randint(0, len(POSSIBLE_ENEMIES[area]["Enemies"]) - 1)]))
        print("A", enemies[i]["Name"], "appeared")

    enter_to_continue()

    if player_area == "tutorial":
        print("You take turns attacking each other")
        enter_to_continue()

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

            enter_to_continue()

            print("Your turn")
            print("----------")

            time.sleep(1)

            print("Your moves: ")
            print("---------------")

            if player_area == "tutorial":
                print("You will have a choice of options to attack the enemy")
                print("Each move has a type. Depending on the enemy, it may be weak or strong against the type")
                print("If you hit a enemies weakness it will do more damage")
                print("If you hit a enemies strength it will do less damage")
                enter_to_continue()
                print("Some moves will be able to hit multiple enemies")
                print("These moves will have [hit multiple enemies - true]")
                enter_to_continue()
                print("When you use a move it will deplete your stamina")
                print("Different moves require different amounts stamina to use")
                print("You can rest to gain some stamina back")
                enter_to_continue()

            weapon_info = player_equipment["Weapon"]["Info"]

            # prints moves
            show_moves(weapon_info)

            item_use = 0
            move_selection_max_length = 0
            if len(item_inventory) > 0:
                move_selection_max_length = 2
            else:
                move_selection_max_length = 1

            # choosing what to do
            while True:
                choose_move = input("Choose move to attack the enemy: ")
                try:
                    choose_move = int(choose_move)
                    if choose_move >= 1 and choose_move <= len(weapon_info) + move_selection_max_length:

                        if choose_move == len(weapon_info) + 1:

                            # this is for the tutorial
                            if player_area == "tutorial":
                                print("You should attack the enemy")
                            else:
                                choose_move = "Rest"
                                break

                        elif choose_move == len(weapon_info) + 2:

                            # inventory use or not or use item check
                            # so that it can go back to move selection
                            for i in range(0, len(item_inventory)):
                                print("Type", i + 1, "to use", item_inventory[i]["Name"], "| Healing -", item_inventory[i]["Healing amount"], "health |")
                                print()
                            print("Type [back] to go back to move selection")
                            print()

                            while True:
                                player_item_input = input("Choose item:")

                                try:
                                    player_item_input = int(player_item_input)
                                    if player_item_input >= 1 and player_item_input <= len(item_inventory):
                                        choose_move = "Inventory"
                                        player_item_input = player_item_input - 1
                                        item_use = item_inventory[player_item_input]
                                        item_inventory.pop(player_item_input)
                                        print("You are using", item_use["Name"])
                                        enter_to_continue()
                                        break
                                    else:
                                        print("Not an option")
                                except ValueError:
                                    if player_item_input.lower() == "back":
                                        print("Going back to move selection")
                                        time.sleep(1.5)
                                        show_moves(weapon_info)
                                        break
                                    elif player_item_input.lower() == "quit":
                                        quit_game()
                                    else:
                                        print("Not an option")

                            # this checks if you used an item
                            # it will break out of the move selection loop
                            # this is here to stop going back to move selection breaking the game
                            if item_use != 0:
                                break


                        # if you choose a move
                        # it will check if you have enough stamina to use it
                        # if so it will break out of the loop
                        # if not it will ask you to input again
                        else:
                            choose_move = choose_move - 1
                            choose_move = player_equipment["Weapon"]["Info"][choose_move]
                            if (player["Stats"]["Stamina"] - choose_move["Stamina use"]) >= 0:
                                break
                            else:
                                print("Not enough stamina to use this move")
                    else:
                        print("Not a valid move")


                # error detection and checking if player wants to quit
                except ValueError:
                    if choose_move.lower() == "quit":
                        quit_game()
                    else:
                        print("Not a number")

            # gain stamina or enemy selection


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

            else:
                target = []

                # enemy selection
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
                # also removes enemies from list if dead
                for i in range(0, len(target)):
                    damage_calculate(target[i][0], choose_move, "Player")
                    # after damage calculation it checks if it is dead and if it is it will remove it from the enemies list
                    if target[i][0]["Stats"]["Health"] <= 0:
                        enemies.remove(target[i][0])

        # checks if you have killed all the enemies
        if len(enemies) == 0:
            print("You won the battle")
            time.sleep(1)
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

        # equiping armour/weapons
        if player_input == 1:
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

                    if one_time_input == last_number:
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
                        player_spare_equipment["Weapons"].pop(one_time_input)
                        player_equipment["Weapon"] = player_spare_equipment["Weapons"][one_time_input]

                    elif one_time_input > len(player_spare_equipment["Weapons"]):
                        # index the variable
                        one_time_input = one_time_input - len(player_spare_equipment["Weapons"]) - 1

                        print("You are equiping", player_spare_equipment["Armour"][one_time_input]["Name"])
                        time.sleep(1)
                        print("You put", player_equipment["Armour"]["Name"], "into your spare equipment")
                        time.sleep(1)

                        player_spare_equipment["Armour"].append(player_equipment["Armour"])
                        player_spare_equipment["Armour"].pop(one_time_input)
                        player_equipment["Armour"] = player_spare_equipment["Armour"][one_time_input]
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

                # one_time_input is NOT IN INDEX FORM
                print(one_time_input)

                if one_time_input == last_number:
                    print("You did not buy anything")
                    time.sleep(2)
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
                time.sleep(2)

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

                    if one_time_input == last_number:
                        print("You did not sell anything")
                        time.sleep(2)
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

                one_time_input -= 1
                if one_time_input == last_number:
                    print("You did not buy anything")
                    break

                if POSSIBLE_ITEMS[shop_area][one_time_input]["Cost"] <= player_money:
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

                    if one_time_input == last_number:
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
print("-------------------------------")
print("You can type quit at any of the inputs to quit the program")
print("-------------------------------")
enter_to_continue()

print("Ganbalf has sent you on a quest to destroy a ring and save middle earth from Zauron")
print("You must venture to Mount Dooom where you can destroy the ring")

enter_to_continue()

print("-------------------------------")
print("Choose your character")
print("-------------------------------")

time.sleep(2)

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
print()
while True:
    player_class_choice = input("Choose a character: ")
    try:
        player_class_choice = int(player_class_choice)
        if player_class_choice >= 1 and player_class_choice <= len(POSSIBLE_CLASSES):
            player_class_choice = player_class_choice - 1
            print("You chose: ", POSSIBLE_CLASSES[player_class_choice]["Name"])
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

print("-------------------------------")
print("Ganbalf has also supplied you a choice of weapons")
print("Choose one")
print("-------------------------------")

time.sleep(3)

for x in range(0, len(POSSIBLE_WEAPONS["tutorial"])):
    print("Armour", x + 1, ":", POSSIBLE_WEAPONS["tutorial"][x]["Name"])
    print("Info: ")
    print_weapon_stats(POSSIBLE_WEAPONS["tutorial"][x])

for i in range(0,len(POSSIBLE_WEAPONS[player_area])):
    print("Type", i+1, "for", POSSIBLE_WEAPONS[player_area][i]["Name"])

while True:
    player_weapon_choice = input("Choose a weapon: ")
    try:
        player_weapon_choice = int(player_weapon_choice)
        if player_weapon_choice >= 1 and player_weapon_choice <= 3:
            player_weapon_choice = player_weapon_choice - 1
            print("You choose: ", POSSIBLE_WEAPONS[player_area][player_weapon_choice]["Name"])
            player_equipment["Weapon"] = POSSIBLE_WEAPONS[player_area][player_weapon_choice]
            break
        else:
            print("Not a valid input")
    except ValueError:
        if player_weapon_choice.lower() == "quit":
            quit_game()
        else:
            print("Not an number")

# this is debugging stuff
# remember to change player money to 0 instead of 99999
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
player_drop_inventory.append({"Name": "Wolf skin", "Cost": 5})
player_spare_equipment["Armour"].append(POSSIBLE_ARMOUR["Shop 1"][0])
player_spare_equipment["Weapons"].append(POSSIBLE_WEAPONS["Shop 1"][0])
enter_shop("Shop 1")
# delete to here
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

enter_to_continue()

print("You are currently at Hobbitown")
print("To reach Mount Dooom you must follow the main road")

time.sleep(2)

print("As you travel down the main road you notice something")
time.sleep(1.5)
print("A stubborn rogue sheep is blocks the way")

time.sleep(1.5)

print("Type 1 to fight the sheep")
print("Type 2 to run around the sheep")
one_use_answer = int_error_detection(": ", [1,2])

if one_use_answer == 1:
    print("You chose to fight the sheep")
elif one_use_answer == 2:
    print("You tried to run around but the sheep attacked you")

time.sleep(1.5)
battle(player_area)

player_drop_inventory.append(POSSIBLE_ENEMIES_DROPS["stubborn rogue sheep"])
print("You got", POSSIBLE_ENEMIES_DROPS["stubborn rogue sheep"]["Name"])
time.sleep(1.5)
print("When you defeat enemies you can gain items")
time.sleep(1.5)
print("These items can be sold to a shopkeeper for money")

enter_to_continue()

print("You continue following the road")
time.sleep(1)
print("There seem to be a group of goblins blocking the way")
time.sleep(1)

print("What should you do")
print("Type 1 - follow the main road and face the group of goblins")
print("type 2 - go around them through the forest")

one_use_answer = int_error_detection(": ", [1,2])

print()

if one_use_answer == 1:
    print("You chose to follow the main road")
    time.sleep(1)
    print("The goblins were threaten by your presences and decided to attack you")
    player_area = "main road 1"
elif one_use_answer == 2:
    print("You decided to go through the forest")
    player_area = "forest 1"

time.sleep(1.5)
battle(player_area)

if player_area == "forest 1":
    player_drop_inventory.append(POSSIBLE_ENEMIES_DROPS["wolf"])
    print("You got wolf skin from defeating the pack of wolves")
    time.sleep(1.5)
    print("You decided to go back on the road")
    player_area = "main road"

    enter_to_continue()
    print("You continue travelling down the road")
    time.sleep(1.5)
    print("You see a goblin gang coming towards you")

elif player_area == "main road 1":
    player_money += 5
    print("You got 5 dollars from defeating the goblins")
    time.sleep(1.5)
    print("You decided to continue following the main road")
    player_area = "main road"
    enter_to_continue()
    print("The previous group of goblins have come back with reinforcements")

time.sleep(1.5)
print("You are attacked by a goblin gang")
time.sleep(1.5)

battle(player_area)
player_money += 7
print("You got 7 dollars from defeating the goblin gang")


player_area = "main road final"

print("You are coming up to the first town in your journey")
time.sleep(1.5)
print("However, there seems to be a goblin giant blocking the entrance")
time.sleep(1)
print("There is no way around")

while True:
    one_time_input = input("Are you prepared to fight it (yes/no): ")
    one_time_input = one_time_input.lower()
    if one_time_input == "yes":
        break
    elif one_time_input == "no":
        print("You waited around, excepting the goblin giant to move")
        time.sleep(2)
        print("The goblin giant didn't move")
        time.sleep(2)
    elif one_time_input == "quit":
        quit_game()
    else:
        print("Not an option")

battle(player_area)
print("You defeated the goblin giant")
player_money += 10
print("The goblin giant dropped 10 dollars")

enter_to_continue()

print("You arrived at _________ town")
print("There seems to be a shop that you can stock up on equipment")
enter_to_continue()

print("Type 1 - go the shop")
print("Type 2 - continue the quest")
one_use_answer = int_error_detection(": ", [1,2])

if one_use_answer == 1:
    enter_shop("Shop 1")
elif one_use_answer == 2:
    print('You continue on with the quest')

print("Hello github make this change")
print("test 2")

