gamee = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
also_no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]


def verifyWinner(game):
    if game[0][0] == game[1][1] and game[0][0] == game[2][2] and game[0][0] > 0:
        print('The winner is player {}'.format(game[0][0]))
        
    elif game[0][2] == game[1][1] and game[0][2] == game[2][0] and game[0][2] > 0:
        print('The winner is player {}'.format(game[0][2]))
        
    elif game[0][0] == game[0][1] and game[0][0] == game[0][2] and game[0][0] > 0:
        print('The winner is player {}'.format(game[0][0]))
        
    elif game[1][0] == game[1][1] and game[1][0] == game[1][2] and game[1][0] > 0:
        print('The winner is player {}'.format(game[1][0]))
        
    elif game[2][0] == game[2][1] and game[2][0] == game[2][2] and game[2][0] > 0:
        print('The winner is player {}'.format(game[2][0]))
        
    elif game[0][0] == game[1][0] and game[0][0] == game[2][0] and game[2][0] > 0:
        print('The winner is player {}'.format(game[0][0]))
        
    elif game[0][1] == game[1][1] and game[0][1] == game[2][1] and game[0][1] >0:
        print('The winner is player {}'.format(game[0][1]))
        
    elif game[0][2] == game[1][2] and game[0][2] == game[2][2] and game[0][2] > 0: 
        print('The winner is player {}'.format(game[0][2]))
    else:
        print("Game over- no winner")


verifyWinner(gamee)
verifyWinner(winner_is_2)
verifyWinner(winner_is_1)
verifyWinner(winner_is_also_1)
verifyWinner(no_winner)
verifyWinner(also_no_winner)
