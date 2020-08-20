# Board
# Display board
# play game
# handle turn
# check win
    # check rows
    # check collums
    # check diagonals
# check tie
# flip players
import msvcrt as m
board = ['-','-','-','-','-','-','-','-','-']
game_still_going = True
winner = None
current_player = 'X'
br = False
def wait():
    m.getch()
def display_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    
def play_game():
    # display the initial board
    display_board()
    global winner
    global br
    while game_still_going:
        handle_turn(current_player)
        
        check_if_game_over()
        if br == True:
            break
        flip_player()
        # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' has won.')
        wait()
    if winner == None:
        print('Tie.')
        wait()

        
def handle_turn(player):
    print(player + "'s Turn.")
    pos = input('Choose a position from 1-9: ')
    
    valid = False
    while not valid:
        
        while pos not in ['1','2','3','4','5','6','7','8','9']:
            pos = input('Invalid input.\nChoose a position from 1-9: ')
        pos = int(pos)-1
        if board[pos] == '-':
            valid = True
        else:
            print("You cant go there. Go again.")
    board[pos] = player
    display_board()
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    global winner
    global br
    #check rows
    row_winner = check_rows()
    #check collums
    collum_winner = check_collums()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
        br = True
    elif collum_winner:
        #there was a win
        winner = collum_winner
        br = True
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
        br = True
    else:
        #there was no win
        winner = None

def check_rows():
    global game_stil_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def check_collums():
    global game_stil_going
    collum_1 = board[0] == board[3] == board[6] != '-'
    collum_2 = board[1] == board[4] == board[7] != '-'
    collum_3 = board[2] == board[5] == board[8] != '-'
    
    if collum_1 or collum_2 or collum_3:
        game_still_going = False
    if collum_1:
        return board[0]
    elif collum_2:
        return board[1]
    elif collum_3:
        return board[2]
    else:
        return None
    
def check_diagonals():
    global game_stil_going
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[2] == board[4] == board[6] != '-'
    
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    else:
        return None
    
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

play_game()