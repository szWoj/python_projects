import random
import math

#one game of rock paper scissors
def play():
    user = input("What's your choice? 'r' 'p' or 's'\n")
    user = user.lower()

    computer = random.choice(["r", "p", "s"])

    #code to decide who wins
    ##we will return 0 for tie, user, computer to be displayed
    if user == computer:
        return (0, user, computer) ## "You and computer have both chosen {}. It's a tie.".format(computer)

    #helper function to determine if user wins against computer
    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)##"You have chosen {} and the computer has chosen {}. You won!".format(user, computer)
    return (-1, user, computer)##"You have chosen {} and the computer has chosen {}. You lost!".format(user, computer)

#let's define this function
def is_win(player, opponent):
    #return true if the player beats the opponent
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    return False


#you wont the best out of n games if you won at least half of them,
#play against the computer until someone wins best of n games
# to win you must win ceil(n/2) (ie. 2/3, 3/5, 3/6, 4/7)
def play_best_of(n):
    
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    #we gotta use while loop because we dont know how many iteration we will need for the
    #game to be complited
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        ## we calling the main play function - which returns 3 things -
        ## 1) result of this particular game(0-tie, 1-user win, -1- computer win)
        ## 2) user choice 3) computer choice
        result, user, computer = play()

        ##tie
        if result == 0:
            print("You and computer have both chosen {}. It's a tie. \n".format(computer))
        ## you win
        elif result == 1:
            player_wins += 1
            print("You have chosen {} and the computer has chosen {}. You won! \n".format(user, computer))
        ## computer wins
        else:
            computer_wins += 1
            print("You have chosen {} and the computer has chosen {}. You lost! \n".format(user, computer))
    ## when you get out of while loop, you know that player_wins got more than wins_necassary
    ## or computer_wins got more than wins_necassary
    if player_wins > computer_wins:
        print("You have won best of {} games. Congrats!\n".format(n))
    else:
        print("Unfortunately, the computer has won the best of {} games \n".format(n))


if __name__ == '__main__':
    play_best_of(3)
