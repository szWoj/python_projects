import random

def random_number():
    random_n = random.randint(1,10)
    return random_n

num_of_tries = 0
random_num = random_number()

while True:
    
    guessed_number = int(input("Guess the number from 1 to 10, 0 to exit"))
    
    if guessed_number == 0:
        break

    elif guessed_number > 10 or guessed_number < 0:
        print("You are out of range")
        num_of_tries += 1
        continue

    else:
        if guessed_number < random_num:
            print("Too low, try again")
            num_of_tries += 1
            continue
        elif guessed_number > random_num:
            print("To high, try again")
            num_of_tries += 1
            continue
        else:
            print("")
            print("That's the right number")
            print("You've guessed the right number in {} tries".format(num_of_tries))
            print("")
            random_num = random_number()
            num_of_tries = 0
            continue
