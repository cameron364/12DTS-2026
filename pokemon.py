import random


wild_pokemon = [
    {"Name": "Charizard", "Type": "Fire", "Level": random.randint(1,3), "Health": random.randint(15,25)},
    {"Name": "Venasuar", "Type": "Grass", "Level": random.randint(1,3), "Health": random.randint(18,22)},
    {"Name": "Blastoise", "Type": "Water", "Level": random.randint(1,3), "Health": random.randint(12,30)},
    {"Name": "Raichu", "Type": "Electric", "Level": random.randint(1,3), "Health": random.randint(10,20)},
    {"Name": "Mr Mime", "Type": "Psychic", "Level": random.randint(1,3), "Health": random.randint(11,21)},
    {"Name": "Jigglypuff", "Type": "Fiary", "Level": random.randint(1,3), "Health": random.randint(12,22)}
]

def battle():
    x=random.randint(0,len(wild_pokemon)-1)
    pokemon = wild_pokemon[x]
    print("A wild", pokemon["Name"], "appeared")
    print("It's a", pokemon["Type"], "type Pokemon")
    print("It's level", pokemon["Level"])
    print("It has", pokemon["Health"], "health")



battle()