flag = False


num = int(input("Is your number prime?"))


for i in range(2,num):
    if (num % i) == 0:
        print(num,"is not a prime number")
        print(i,"times",num//i,"is",num)
        flag = True    
        break
else:
        
    print(num,"is a prime number")
    

if flag:
    print(f"Number {num} is NOT prime")
else:
    print(f"Number {num} is prime")



