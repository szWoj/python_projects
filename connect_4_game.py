import numpy as np
import pygame

ROW_COUNT = 6
COLUMN_COUNT = 7




# creating a board of zeros
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece
    

# top row of my matrix must be zero to be valid
def is_valid_location(board, col):
    return board[5][col] == 0

# checking which row the piece will fall into
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
# function which changes orientation
def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):

    # check all horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # check for vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # chech for diagonal incresing/positive
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # chech for diagonal decresing/negative
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    
board = create_board()
print_board(board)
game_over = False
# turn will determine who's turn (Player1 or Player2) it is to play
turn = 0

###initializing our project
##pygame.init()
##
##SQUARESIZE = 100
##width = COLUMN_COUNT * SQUARESIZE
##height = (ROW_COUNT + 1) * SQUARESIZE
##
##size = (width, height)
##
###to get pygame to read that we need this (from pygame documentations):
##screen = pygame.display.set_mode(size)






while not game_over:


    # Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True

    # Ask Player 2 input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 2 wins!")
                game_over = True
            
    print_board(board)

    # It doesn't matter who's turn it was, we want to increment turn
    turn += 1
    # It will rotate between 0 and 1
    turn = turn % 2
