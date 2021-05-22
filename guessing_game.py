from random import randint 

num = randint(1,100)
num_of_tries = 0

print("Welcome to the guessing game")

while True:
    try:
        guess = int(input("guess the number from 1-100, 0 to exit"))
        num_of_tries += 1
        
    except:
        print("you are not putting number")
        continue

    if guess == 0:
        break
    elif guess < 1 or guess > 100:
        print("you are out of range")

    else:
        if num == guess:
            print("You won in " + str(num_of_tries) + ". Congrats!!")
            again = input("Wanna play again? If so input y, for no anything else")
            if again == "y" or again == "Y":
                num_of_tries = 0
                num = randint(1,100)
            else:
                break
        else:
            if guess > num:
                print("too high, try again")
            else:
                print("too low, try again")
                
print("Thanks for playing, we hope you will come back soon")
