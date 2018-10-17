import random

def draw_board(board):
    #gets the board's list and print it
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    #asks the player if he wants X or O
    #return list [player's letter, computer's letter]
    letter = ''
    while not (letter=='X' or letter=='O'):
        print("Do you want to be X or O")
        letter = input().upper()

    if letter == 'X':
        return['X', 'O']
    else:
        return ['O', 'X']

def who_starts():
    #randomisly deciding who will start the game
    #returns 'player' if the player will start and 'computer' if computer will start
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'

def is_space_free(move, board):
    #returns true if the space is free on the board
    return board[move] == ' '

def get_player_move(board):
    #gets the position the player wants to go to
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(int(move), board):
        print('what is your move (1-9)')
        move = input()
    return int(move)

def make_move(board, move, letter):
    board[int(move)] = letter

def is_winner(board, letter):
    #Retruns true if ther is a winner
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or #top line
    (board[4] == letter and board[5] == letter and board[6] == letter) or #middle line
    (board[1] == letter and board[2] == letter and board[3] == letter) or #bottom line
    (board[1] == letter and board[4] == letter and board[7] == letter) or #left row
    (board[2] == letter and board[5] == letter and board[8] == letter) or #middle row
    (board[3] == letter and board[6] == letter and board[9] == letter) or #right row
    (board[1] == letter and board[5] == letter and board[9] == letter) or #diagonal
    (board[3] == letter and board[5] == letter and board[7] == letter)) #diagonal

def board_copy(board):
    #Retruns copy of a given board
    copy = []
    
    for i in board:
        copy.append(i)

    return copy

def choose_random_move_from_list(board, move_list):
    #Returns random move from valid move from move list
    #Returns None if there's no valid move
    possibles = []
    for i in move_list:
        if is_space_free(i, board):
            possibles.append(i)
    if len(possibles) != 0:
        return random.choice(possibles)
    else:
        return None
        
    
def get_computer_move(board, computer_letter):
    #AI 
    if computer_letter == 'X':
        player_letter == 'O'
    else:
        player_letter == 'X'

    #Checks if AI can win in next move
    for i in range(1, 10):
        temp = board_copy(board)
        if is_space_free(i, temp):
            make_move(temp, i, computer_letter)
            if is_winner(temp, computer_letter):
                return i
        
    #Checks if player can win in next round
    for i in range(1, 10):
        temp = board_copy(board)
        if is_space_free(i, temp):
            make_move(temp, i ,player_letter)
            if is_winner(temp, player_letter):
                return i

    #Checks if one of the corners is empty
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    #Checks if the center is empty
    if is_space_free(5, board):
        return 5

    #Move to one of the sides
    return choose_random_move_from_list(board, [2 ,4 ,6 ,8])

def is_board_full(board):
    #return true if every space on the board is full
    for i in range(1, 10):
        if is_space_free(i, board):
            return False
    return True

def play_again():
    #Returns true if players wants to play again
    print('Do you want to play again (yes or no)')
    return input().lower().startswith('y')


while True:
    board = [' '] * 10 # resets the board
    player_letter, computer_letter = input_player_letter()
    turn = who_starts()
    print('The ' + turn + ' will go first.')
    is_playing = True
    while is_playing:
        
        if turn == 'player':
            #player's turn
            draw_board(board)
            move = get_player_move(board)
            make_move(board, move, player_letter)

            if is_winner(board, player_letter):
                draw_board(board)
                print('WOOOOOOOOOOOOW YOU HAVE WON THE GAME!!!!')
                is_playing = False
            else:
                if is_board_full(board):
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            #computer's turn
            move = get_computer_move(board, computer_letter)
            make_move(board, move, computer_letter)
            if is_winner(board, computer_letter):
                draw_board(board)
                print('OHHH YOU LOST :( !!!!')
                is_playing = False
            else:
                if is_board_full(board):
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
                    

    if not play_again():
        break




















