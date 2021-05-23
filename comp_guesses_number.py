import random

lst = [i for i in range(100)]

my_number = 89
tries = 1

while True:
    index = int((len(lst) +1) / 2)
    comp_guess = lst[index]
    if comp_guess == my_number:
        print(comp_guess ,"computer guessed in " + str(tries) + "tries")
        break
    elif comp_guess < my_number:
        print(comp_guess, "computer keep trying")
        lst = lst[ index :]
       
        tries += 1
        continue
    else:
        print(comp_guess, "computer keeps trying")
        lst = lst[ : index ]
        
        tries += 1
        continue
    


