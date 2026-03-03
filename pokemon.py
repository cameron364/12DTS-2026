# libraries
import random
import time

# Variables
wild_pokemon = [
    {"Name": "Charizard", "Type": "Fire", "Level": random.randint(1,3), "Health": random.randint(15,25), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Venasuar", "Type": "Grass", "Level": random.randint(1,3), "Health": random.randint(18,22), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Blastoise", "Type": "Water", "Level": random.randint(1,3), "Health": random.randint(12,30), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Raichu", "Type": "Electric", "Level": random.randint(1,3), "Health": random.randint(10,20), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Mr Mime", "Type": "Psychic", "Level": random.randint(1,3), "Health": random.randint(11,21), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Jigglypuff", "Type": "Fiary", "Level": random.randint(1,3), "Health": random.randint(12,22), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]}
]
# Functions
own_pokemon = [
    {"Name": "Pidgy1", "Type": "Flying", "Level": 3, "Health": 30, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy2", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy3", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy4", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy5", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy6", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]}
]

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
            randomnum = random.randrange(0,3,2)
            enemy_attack_randomiser_name = pokemon["Attack"][randomnum]
            enemy_attack_randomiser_damage = pokemon["Attack"][randomnum+1]
            print()
            print(pokemon["Name"],"used",enemy_attack_randomiser_name,"it did",enemy_attack_randomiser_damage,"damage")

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

            for i in range(0,len(player_pokemon["Attack"]),2):
                if i == 0:
                    print("Type 1 for", player_pokemon["Attack"][i])
                if i == 2:
                    print("Type 2 for", player_pokemon["Attack"][i])
                if i == 4:
                    print("Type 3 for", player_pokemon["Attack"][i])
                if i == 6:
                    print("Type 4 for", player_pokemon["Attack"][i])

                if i == len(player_pokemon["Attack"])/2:
                    print("Type",int((i/2)+2),"to run")
                    print("Type", int((i / 2) + 3), "to do nothing")


            while True:
                try:
                    choose_move = int(input(": "))
                    if choose_move <= (len(player_pokemon["Attack"])/2)+2 and choose_move > 0:
                        break
                    else:
                        print("Not an option")
                except ValueError:
                    print("Error")

            print()
            if choose_move == (len(player_pokemon["Attack"])/2)+1:
                print("You ran away")
                break
            elif choose_move == (len(player_pokemon["Attack"])/2)+2:
                player_pokemon_move_name = "nothing"
                player_pokemon_move_damage = 0
            else:
                choose_move = choose_move*2-2
                player_pokemon_move_name = player_pokemon["Attack"][choose_move]
                player_pokemon_move_damage = player_pokemon["Attack"][choose_move+1]


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