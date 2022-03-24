# This program allows the user to play a game called Two Squares.
# They enter the rectangle by choosing two squares one by one.
# The numbers have to be next to each other. The last player to put a rectangle wins.
# Author: Selsabeel Asim Ali Elbagir
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
# a list containing the numbers in the 4x4 squares

def display_board():
    print (" ------------------")
    print ("| ", board [0], " | ", board [1], " | ", board [2], " | ", board[3], " | ")
    print (" ------------------")
    print ("| ", board [4], " | ", board [5], " | ", board [6], " | ", board[7], " | ")
    print (" ------------------")
    print ("| ", board [8], " | ", board [9], " | ", board [10], " | ", board [11], " | ")
    print (" ------------------")
    print ("| ", board [12], " | ", board [13], "| ", board [14], " | ", board [15], " | ")
# the board itself

def get_player_action (player):
    is_valid = False
    message = "Please choose two cells next to each other from 1 to 16 for player " + player + ": "
    while (not is_valid):
        action = input(message)
        if not action.isdigit(): #this is to ensure that the user enters only numbers
            continue
        else:
            is_valid = True
            action = int(action)
            is_valid = is_valid and int(action) > 0 and int(action) <= 16
            #this is to ensure the user picks a number between 0 and 16
            is_valid = is_valid and board[action -1] != 'X'
            #this ensures that the square chosen hasn't been chosen before
    return action

def update_game_board (action, player):
    board [action - 1] = player
    display_board()

def is_winner(n_actions,board):
    if n_actions > 16:
        return True
    else:
        remaining = []
        for x in board:
            if x.isdigit():
                x=int(x)
                remaining.append(x) #puts all of the remaining squares into an array
        for num in remaining:
            x1 = (num) + 4
            x2 = (num) - 4
            x3 = (num) + 1
            x4 = (num) - 1
            #now we make sure that there are still possible combinations from the remaining squares to pick
            if (x1 in remaining)or (x2 in remaining) or (x3 in remaining) or (x4 in remaining):
                return False

        return True



def play_game():
    display_board()
    n_actions = 0
    while n_actions < 16:
        action = get_player_action('1')
        update_game_board(action, 'X')
        n_actions += 1

        validaction = False
        while validaction == False:
            action2 = get_player_action('1')
            validaction = ((action2 == action + 4) or (action2 == action - 4) or (action2 == action + 1) or (
                    action2 == action - 1)) #this ensures that the second square the user chose is next to it
        update_game_board(action2, 'X')
        n_actions += 1
        if (is_winner(n_actions, board)) == True:
            print('Congratulations, player 1! You won.')
            return

        action = get_player_action('2')
        update_game_board(action, 'X')
        n_actions += 1

        validaction = False
        while validaction == False:
            action2 = get_player_action('2')
            validaction = ((action2 == action + 4) or (action2 == action - 4) or (action2 == action + 1) or (
                    action2 == action - 1))
        update_game_board(action2, 'X')
        n_actions += 1
        if (is_winner(n_actions, board)) == True:
            print('Congratulations, player 2! You won.')
            return



play_game()