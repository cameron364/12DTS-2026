# libraries
import random
import time

# Variables
wild_pokemon = [
    {"Name": "Charizard", "Type": "Fire", "Level": random.randint(1,3), "Health": random.randint(15,25), "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Venasuar", "Type": "Grass", "Level": random.randint(1,3), "Health": random.randint(18,22), "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Blastoise", "Type": "Water", "Level": random.randint(1,3), "Health": random.randint(12,30), "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Raichu", "Type": "Electric", "Level": random.randint(1,3), "Health": random.randint(10,20), "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Mr Mime", "Type": "Psychic", "Level": random.randint(1,3), "Health": random.randint(11,21), "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Jigglypuff", "Type": "Fairy", "Level": random.randint(1,3), "Health": random.randint(12,22), "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]}
]
# Functions
own_pokemon = [
    {"Name": "Pidgy1", "Type": "Flying", "Level": 3, "Health": 30, "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Pidgy2", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Pidgy3", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Pidgy4", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Pidgy5", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]},
    {"Name": "Pidgy6", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Fire", "Solar Beam", random.randrange(7,9), "Grass"]}
]
weak_and_resist_info = {"Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Bug": 2, "Rock": 0.5, "Dragon": 0.5, "Steel": 2},
                        "Grass": {"Fire": 0.5, "Water": 2, "Grass": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Bug": 0.5, "Rock": 2, "Dragon": 0.5, "Steel": 0.5}
                        }

def weak_and_resist(attacking, defending):
    try:
        damage_multi = weak_and_resist_info[attacking][defending]
    except:
        damage_multi = 1
    return damage_multi


def overworld_timer():
    timer = random.randint(0,1)
    print(timer)
    time.sleep(timer)
    print("Battle begins")
    battle()


def battle():
    x=random.randint(0,len(wild_pokemon)-1)
    pokemon = wild_pokemon[x]
    player_pokemon = own_pokemon[0]
    player_pokemon_hp = player_pokemon["Health"]
    # show player pokemon
    print("Player pokemon:",player_pokemon["Name"])
    print("Player pokemon health:",player_pokemon_hp)
    # show enemy pokemon
    print("A wild", pokemon["Name"], "appeared")
    print("It's a", pokemon["Type"], "type Pokemon")
    print("It's level", pokemon["Level"])
    print("It has", pokemon["Health"], "health")

    #batte

    while True:
        try:
            fight = int(input("Do you want to fight 1-yes 2-no: "))
        except ValueError:
            print("Error")

        if fight > 2:
            print("Wrong number")
        elif fight < 0:
            print("Wrong number")

        elif fight == 2:
            overworld_timer()
        elif fight == 1:
            print("You chose to battle")
            break

    for i in range(0, 10):
        print()

    while True:
        # AI attack code
        if pokemon["Health"] > 0:
            randomnum = random.randint(0,(len(pokemon["Attack"])/3)-1)
            enemy_attack_randomiser_name = pokemon["Attack"][randomnum*3]
            enemy_attack_randomiser_damage = pokemon["Attack"][(randomnum*3)+1]
            enemy_attack_randomiser_type = pokemon["Attack"][(randomnum*3)+2]

            # weakness checker
            attack_mulitplier = weak_and_resist(enemy_attack_randomiser_type,player_pokemon["Type"])
            enemy_attack_randomiser_damage = int(enemy_attack_randomiser_damage * attack_mulitplier)

            if attack_mulitplier == 1:
                print()
                print(pokemon["Name"], "used", enemy_attack_randomiser_name, "it did", enemy_attack_randomiser_damage, "damage")
            elif attack_mulitplier == 2:
                print()
                print(pokemon["Name"], "used", enemy_attack_randomiser_name, "it is , it did", enemy_attack_randomiser_damage, "damage")
            elif attack_mulitplier == 0.5:
                print()
                print(pokemon["Name"], "used", enemy_attack_randomiser_name, "it is weak, it did", enemy_attack_randomiser_damage, "damage")



            player_pokemon_hp = player_pokemon_hp - enemy_attack_randomiser_damage
            print()
            print(player_pokemon["Name"],"is at",player_pokemon_hp,"health")
        else:
            print(pokemon["Name"],"died")
            print("Leaving battle")
            time.sleep(1)
            break

        if player_pokemon_hp > 0:
            print()
            print("Your turn")
            print("Which move")

            for i in range(0,len(player_pokemon["Attack"]), 3):
                if i == 0:
                    print("Type 1 for", player_pokemon["Attack"][i])
                if i == 3:
                    print("Type 2 for", player_pokemon["Attack"][i])
                if i == 6:
                    print("Type 3 for", player_pokemon["Attack"][i])
                if i == 9:
                    print("Type 4 for", player_pokemon["Attack"][i])

                if i == len(player_pokemon["Attack"])/2:
                    print("Type",int((i/3)+2),"to run")
                    print("Type", int((i / 3) + 3), "to do nothing")


            while True:
                try:
                    choose_move = int(input(": "))
                    if choose_move <= (len(player_pokemon["Attack"])/3)+2 and choose_move > 0:
                        break
                    else:
                        print("Not an option")
                except ValueError:
                    print("Error")


            if choose_move == (len(player_pokemon["Attack"])/3)+1:
                print("You ran away")
                break
            elif choose_move == (len(player_pokemon["Attack"])/3)+2:
                player_pokemon_move_name = "nothing"
                player_pokemon_move_damage = 0
            else:
                choose_move = choose_move*3-2
                player_pokemon_move_name = player_pokemon["Attack"][choose_move-1]
                player_pokemon_move_damage = player_pokemon["Attack"][choose_move]

            # add the type effect code here
            #attack_mulitplier = weak_and_resist(enemy_attack_randomiser_type, player_pokemon["Type"])
            #enemy_attack_randomiser_damage = int(enemy_attack_randomiser_damage * attack_mulitplier)


            print("You chose", player_pokemon_move_name, "does",player_pokemon_move_damage,"damage")
            print()

            pokemon["Health"] = pokemon["Health"] - player_pokemon_move_damage
            print(pokemon["Name"],"hp is at",pokemon["Health"])

            for i in range(0,10):
                print()

            time.sleep(2)
        else:
            print("pokemon died")
            break


    overworld_timer()










# Main code
overworld_timer()