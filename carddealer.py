import time
import random
hand = [[],[]]
deck = [[],[]]
SUITS = ["Hearts","Clubs","Spades","Diamonds"]
VALUE = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def draw():
    amount = int(input("How many cards draw: "))
    for i in range(0,amount):
        print(len(deck[0]))
        random_num = random.randint(0,len(deck[0]))
        card_drew = [deck[0][random_num],deck[1][random_num]]


        deck[0].pop(random_num)
        deck[1].pop(random_num)

        hand[0].append(card_drew[0])
        hand[1].append(card_drew[1])

def printdeck():
    print("------------ deck ------------")
    for i in range(0, len(deck[0])):
        print("card", i + 1, "is:", deck[0][i], deck[1][i])
    print("------------------------------")
    print()

def printhand():
    print("------------ hand ------------")
    for i in range(0, len(hand[0])):
        print("card", i + 1, "is:", hand[0][i], hand[1][i])
    print("------------------------------")
    print()


print("building deck")
for x in SUITS:
    print("Adding",SUITS,"suit")
    for y in VALUE:
        deck[0].append(x)
        deck[1].append(y)
        print("Card:",y,"of",x,"added")
        time.sleep(0.001)
    print("----Done----")

printdeck()


draw()
printdeck()
printhand()
