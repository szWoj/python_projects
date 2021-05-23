import random

comp_wins = 0
player_wins = 0

def player_game():
    your_choice = input("What do you chose? (rock(r), scissors(s), paper(p)")
    your_choice = your_choice.lower()
    if your_choice in ["rock", "r"]:
        your_choice = "r"
    elif your_choice in ["scissors", "s"]:
        your_choice = "s"
    elif your_choice in ["paper", "p"]:
        your_choice = "p"
    else:
        print("You mistyped, try again")
        player_game()
    return your_choice

def com_game():
    poss = ["r", "s", "p"]
    comp_choice = random.choice(poss)
    return comp_choice


while True:
    print("")
    your_choice = player_game()
    comp_choice = com_game()
    print("")

    if your_choice == "r":
        if comp_choice == "r":
            print("You tied")

        elif comp_choice == "p":
            print("You win, you rock")
            player_wins += 1

        elif comp_choice == "s":
            print("You lose, you were rock")
            comp_wins += 1

    elif your_choice == "s":
        if comp_choice == "s":
            print("You tied")

        elif comp_choice == "p":
            print("You win, you rock")
            player_wins += 1

        elif comp_choice == "r":
            print("You lose, you were scissors")
            comp_wins += 1

    elif your_choice == "p":
        if comp_choice == "p":
            print("You tied")

        elif comp_choice == "r":
            print("You win, you rock")
            player_wins += 1

        elif comp_choice == "s":
            print("You lose, you were a paper")
            comp_wins += 1

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you wanna play again? yes/no ")
    user_choice = user_choice.lower()
    if user_choice in ["yes", "y"]:
        continue
    elif user_choice in ["no", "n"]:
        break
    else:
        break
    
