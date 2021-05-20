count = 2
print("You can check for even number twice ")
while True:
    try:
        
        num = int(input("put a number to check if odd\even"))
        if count == 2:
            break

    except:
        print("You didnt put a number")
        continue

    if num < 1:
        print("Your number is not + ")
        continue

    elif num % 2 ==0:
        print("even number")
        count +=1
        
    else:
        print("Odd number")
        continue

