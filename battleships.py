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

def place_boat(size):
    if size == 2:
        horz_or_vert = input("How do you want to place you boat vert or horz:")
        start_x_position = int(input("What x pos do you want your hull of the ship start: "))



make_board(blue_board)
print_board(blue_board)



