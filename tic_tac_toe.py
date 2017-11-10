board = [
    ["1.", "2.", "3."],
    ["4.", "5.", "6."],
    ["7.", "8.", "9."],
]

player = ["player1", "player2"]
turn = 0

is_playing = True    

def print_board (board):
    for row in board:
        print " ".join(map(str, row))

def change_board(option, value, board):
    if option == "1":
        board[0][0] = value
        print_board(board)
        check_winner(board)
    elif option == "2":
        board[0][1] = value
        print_board(board)
        check_winner(board)
    elif option == "3":
        board[0][2] = value
        print_board(board)
        check_winner(board)
    elif option == "4":
        board[1][0] = value
        print_board(board)
        check_winner(board)
    elif option == "5":
        board[1][1] = value
        print_board(board)
        check_winner(board)
    elif option == "6":
        board[1][2] = value
        print_board(board)
        check_winner(board)
    elif option == "7":
        board[2][0] = value
        print_board(board)
        check_winner(board)
    elif option == "8":
        board[2][1] = value
        print_board(board)
        check_winner(board)
    elif option == "9":
        board[2][2] = value
        print_board(board)
        check_winner(board)


def check_winner(board):
    global turn
    if board[0][0] == board[0][1] == board[0][2] == "X":
        print ""
        print "Player 1 IS THE WINNER!" 
        turn = 0
        reset_board()
    elif board[0][0] == board[0][1] == board[0][2] == "O":
        print ""
        print "Player 2 IS THE WINNER!" 
        turn = 0
        reset_board()
    elif board[0][0] == board[1][0] == board [2][0] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][0] == board[1][0] == board [2][0] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][1] == board[1][1] == board[2][1] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print ""
        print "Player 1 IS THE WINNER!"
        turn = 0
        reset_board()
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        print ""
        print "Player 2 IS THE WINNER!"
        turn = 0
        reset_board()
    

def reset_board():
    global board
    board = [
        ["1.", "2.", "3."],
        ["4.", "5.", "6."],
        ["7.", "8.", "9."],
    ]
    
def process_input(player, input):
    global turn
    if player == "player1":
        turn = 1
        change_board(input, "X", board)
    elif player == "player2":
        turn = 0
        change_board(input, "O", board)


def start():
    global turn, player    
    while is_playing:
        print "Player Turn:", player[turn]
        input = raw_input("Press a number to make a choice: ")
        process_input(player[turn], input)

start()