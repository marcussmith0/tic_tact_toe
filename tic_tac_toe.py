from IPython.display import clear_output

board = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9."]
turn = 0

def display_board(board):
    print ""
    print "   " + board[0] + " | " + board[1]  + " | " +  board[2]
    print "   " + "____________"
    print "   " + board[3] + " | " + board[4]  + " | " +  board[5]
    print "   " + "____________"
    print "   " + board[6] + " | " + board[7]  + " | " +  board[8]
    print ""
    
    player_input()

def player_input():
    global turn
    position = raw_input("Place your marker: ")

    if turn == 0:
        turn = 1
        place_marker("X", position)
    elif turn == 1:
        turn = 0
        place_marker("O", position)

def place_marker(value, place):
    global board
    if place == "1":
        board[0] = value
        check_winner()
        display_board(board)
    elif place == "2":
        board[1] = value
        check_winner()
        display_board(board)
    elif place == "3":
        board[2] = value
        check_winner()
        display_board(board)
    elif place == "4":
        board[3] = value
        check_winner()
        display_board(board)
    elif place == "5":
        board[4] = value
        check_winner()
        display_board(board)
    elif place == "6":
        board[5] = value
        check_winner()
        display_board(board)
    elif place == "7":
        board[6] = value
        check_winner()
        display_board(board)
    elif place == "8":
        board[7] = value
        check_winner()
        display_board(board)
    elif place == "9":
        board[8] = value
        check_winner()
        display_board(board)
    else:
        print "Don't recognized that command."

def reset_board():
    global board
    board = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9."]

def check_winner():
    if board[0] == board[1]  == board[2] == "X":
        print "Player X wins"
        reset_board()
    elif board[0] == board[1]  == board[2] == "O":
        print "Player O wins"
        reset_board()
    elif board[3] == board[4]  == board[5] == "X":
        print "Player X wins"
        reset_board()
    elif board[3] == board[4]  == board[5] == "O":
        print "Player O wins"
        reset_board()
    elif board[6] == board[7]  == board[8] == "X":
        print "Player X wins"
        reset_board()
    elif board[6] == board[7]  == board[8] == "O":
        print "Player O wins"
        reset_board()
    elif board[0] == board[3]  == board[6] == "X":
        print "Player X wins"
        reset_board()
    elif board[0] == board[3]  == board[6] == "O":
        print "Player O wins"
        reset_board()
    elif board[1] == board[4]  == board[7] == "X":
        print "Player X wins"
        reset_board()
    elif board[1] == board[4]  == board[7] == "O":
        print "Player O wins"
        reset_board()
    elif board[2] == board[5]  == board[8] == "X":
        print "Player X wins"
        reset_board()
    elif board[2] == board[5]  == board[8] == "O":
        print "Player O wins"
        reset_board()
    elif board[0] == board[4]  == board[8] == "X":
        print "Player X wins"
        reset_board()
    elif board[0] == board[4]  == board[8] == "O":
        print "Player O wins"
        reset_board()
    elif board[2] == board[4]  == board[6] == "X":
        print "Player X wins"
        reset_board()
    elif board[2] == board[4]  == board[6] == "O":
        print "Player O wins"
        reset_board()


display_board(board)