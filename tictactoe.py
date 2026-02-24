# variables
board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]
turn_counter = 0
# functions


# prints the board
def print_board():
    for i in range(0,3):
        print(board[i])


# in a loop that asks for input
# if not an answer asks again
# turns input into either a x or y position
# removes that spot in the board and replaces it with the o or x
def move(type):
    print()
    print(type, "turns")
    print()
    while True:
        move_x = input("left, mid, right: ")
        move_x.lower()
        pos_x = 0

        move_y = input("top, mid, bottom: ")
        move_y.lower()
        pos_y = 0

        if move_x == "left":
            pos_x = 0
        if move_x == "mid":
            pos_x = 1
        if move_x == "right":
            pos_x = 2

        if move_y == "top":
            pos_y = 0
        if move_y == "mid":
            pos_y = 1
        if move_y == "bottom":
            pos_y = 2

        if board[pos_y][pos_x] == "o" or board[pos_y][pos_x] == "x":
            print("spot taken")
        else:
            board[pos_y].pop(pos_x)
            board[pos_y].insert(pos_x, type)
            break


# stores all the combinations of winning possibilities
def check_win(type):
    if board[0][0] == type and board[0][1] == type and board[0][2] == type:
        return type
    elif board[1][0] == type and board[1][1] == type and board[1][2] == type:
        return type
    elif board[2][0] == type and board[2][1] == type and board[2][2] == type:
        return type

    elif board[0][0] == type and board[1][0] == type and board[2][0] == type:
        return type
    elif board[0][1] == type and board[1][1] == type and board[2][1] == type:
        return type
    elif board[0][2] == type and board[1][2] == type and board[2][2] == type:
        return type

    elif board[0][0] == type and board[1][1] == type and board[2][2] == type:
        return type
    elif board[2][0] == type and board[1][1] == type and board[0][2] == type:
        return type
    elif turn_counter == 9:
        return "tie"


# main code


# loop that continues until game wins or tie
while True:
    move("o")
    turn_counter += 1
    if check_win("o") == "o":
        print("-------")
        print(check_win("o"),"wins")
        print("-------")
        break
    elif check_win("x") == "tie":
        print("-------")
        print("Tie")
        print("-------")
        break
    print_board()

    move("x")
    turn_counter += 1
    if check_win("x") == "x":
        print("-------")
        print(check_win("x"), "wins")
        print("-------")
        break
    elif check_win("x") == "tie":
        print("-------")
        print("Tie")
        print("-------")
        break
    print_board()



