blue_board = []
red_board = []


#functions

# makes boards
def make_board(board):
    for x in range(0,10):
        board.append([])
        for y in range(0,10):
            board[x].append("_")

# print boards
def print_board(board):
    for i in range(0,10):
        print(board[i])

def place_boat(size,board):
    horz_or_vert = input("How do you want to place you boat vert or horz:")
    while True:
        start_x_position = int(input("What x pos do you want your hull of the ship start: "))
        start_y_position = int(input("What y pos do you want your hull of the ship start: "))
        if start_x_position + size > 10:



    if horz_or_vert == "horz":
        board[start_y_position].pop(start_x_position)
        board[start_y_position].insert(start_x_position,"O")
        for i in range(1,size):
            board[start_y_position].pop(start_x_position + i)
            board[start_y_position].insert(start_x_position + i, "O")

    if horz_or_vert == "vert":
        board[start_y_position].pop(start_x_position)
        board[start_y_position].insert(start_x_position,"O")
        for i in range(1,size):
            board[start_y_position+ i].pop(start_x_position )
            board[start_y_position + i].insert(start_x_position, "O")





make_board(blue_board)
print_board(blue_board)

place_boat(4,blue_board)
print_board(blue_board)
