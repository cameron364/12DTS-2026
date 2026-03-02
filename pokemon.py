# libraries
import random
import time

# Variables
wild_pokemon = [
    {"Name": "Charizard", "Type": "Fire", "Level": random.randint(1,3), "Health": random.randint(15,25), "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Venasuar", "Type": "Grass", "Level": random.randint(1,3), "Health": random.randint(18,22)},
    {"Name": "Blastoise", "Type": "Water", "Level": random.randint(1,3), "Health": random.randint(12,30)},
    {"Name": "Raichu", "Type": "Electric", "Level": random.randint(1,3), "Health": random.randint(10,20)},
    {"Name": "Mr Mime", "Type": "Psychic", "Level": random.randint(1,3), "Health": random.randint(11,21)},
    {"Name": "Jigglypuff", "Type": "Fiary", "Level": random.randint(1,3), "Health": random.randint(12,22)}
]
# Functions
own_pokemon = [
    {"Name": "Pidgy1", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy2", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy3", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy4", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy5", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]},
    {"Name": "Pidgy6", "Type": "Flying", "Level": 3, "Health": 15, "Attack": ["Blaze", random.randrange(4,7), "Solar Beam", random.randrange(7,9)]}
]

def overworld_timer():
    timer = random.randint(0,0)
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


    while True:
        # AI attack code
        enemy_attack_randomiser = random.randint(0,len(wild_pokemon[pokemon-1]),2)
        print("Random ")

    while pokemon["Health"] > 0:
        print("Your turn")
        print("Which move")
        for i in range(len(player_pokemon["Attack"])):
            print("Type",i ,"for", player_pokemon["Attack"][i])

        choose_move = int(input(": "))



# Main code
overworld_timer()