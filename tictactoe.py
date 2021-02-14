# board
# display
# playgame
# win func
# tie func
# flip pay

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
play1 = "X"
play2 = "0"
curr_player = play1
winner = None
game_status = True


def disp_board():
    print("     " + board[0] + " | " + board[1] + " | " + board[2])
    print("     " + board[3] + " | " + board[4] + " | " + board[5])
    print("     " + board[6] + " | " + board[7] + " | " + board[8])
    print(" ")


def playgame():
    print("********** TIC - TAC - TOE ***********")
    print("          PLAYER 1 = X")
    print("          PLAYER 2 = 0")
    print(" ")
    disp_board()
    global curr_player
    global winner
    while game_status:
        turn(curr_player)
        check_win()
        flip_player()
    if winner == play1:
        print("PLAYER 1 WONNNN!!!!!!!!")
    elif winner == play2:
        print("PLAYER 2 WON........")
    elif winner is None:
        print("THE GAME IS TIED......LOL")


def flip_player():
    global curr_player
    if curr_player == play1:
        curr_player = play2
    else:
        curr_player = play1


def check_win():
    global game_status
    global winner
    if board[0] == board[1] == board[2] != "-":
        game_status = False
        winner = curr_player
    elif board[3] == board[4] == board[5] != "-":
        game_status = False
        winner = curr_player
    elif board[6] == board[7] == board[8] != "-":
        game_status = False
        winner = curr_player
    elif board[0] == board[3] == board[6] != "-":
        game_status = False
        winner = curr_player
    elif board[1] == board[4] == board[7] != "-":
        game_status = False
        winner = curr_player
    elif board[8] == board[2] == board[5] != "-":
        game_status = False
        winner = curr_player
    elif board[0] == board[4] == board[8] != "-":
        game_status = False
        winner = curr_player
    elif board[2] == board[4] == board[6] != "-":
        game_status = False
        winner = curr_player
    elif board[0] != "-" and board[1] != "-" and board[2] != "-" and board[3] != "-" and board[4] != "-" and board[5] \
            != "-" and board[6] != "-" and board[7] != "-" and board[8] != "-":
        game_status = False


def turn(player):
    ch = int(input("PLAYER " + player + " ENTER YOUR CHOICE IN 1-9 = "))
    if board[ch-1] != "-":
        print("ANOTHER PLAYER ALREADY MARKED THERE!! U LOST UR TURN...LOL")
    else:
        board[ch - 1] = player
    disp_board()


playgame()
