import random

def game():
    random_num = random.randint(1,10)
    return random_num


random_num = game()
tries = 1

while True:
    
    guessed_num = int(input("guess the number from 1 to 100: "))
    

    if guessed_num == random_num:
        print("You got it right in " + str(tries) + " tries")
        break

    elif guessed_num < random_num:
        tries += 1
        print("too low, try again")
        continue

    else:
        tries += 1
        print("too high, try again")
        continue
