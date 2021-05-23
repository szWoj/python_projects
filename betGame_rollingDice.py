from random import randint

cash = 100
bet = 5
while True:
    print("\n---------------------------------")
    print("Place your bet or X to exit")
    print("1) High\t (2x) ")
    print("2) Low\t (2x) ")
    print("3) 7\t (3x)")
    print("Cash on hand: " + str(cash))
    print("-----------------------------------")

    choice = input("Make your choice: ")

    if choice == "X" or choice == "x":
        print("Thanks for playing")
        break
    elif choice == "1" or choice == "2" or choice == "3":

        while True:
            try:
                bet = int(input("Place your bet: "))
            except:
                print("Please enter a number:")
                continue
            if bet > 0 and bet <= cash:
                break
            else:
                print("That bet is not valid")


        
        roll = randint(1,6) + randint(1,6)
        print("You've rolled a " + str(roll))

        if roll > 7 and choice == "1":
            print("You win!")
            cash = cash + bet
        elif roll < 7 and choice == "2":
            print("You win!")
            cash = cash + bet
        elif roll == 7 and choice == "3":
            print("You win!")
            cash = cash + (2 * bet)
        else:
            print("You lose!")
            cash = cash - bet
            if cash == 0:
                print("You have no money left, you are off")
                break



        print(roll)
    else:
        print("Enter a valid choice")
        continue
