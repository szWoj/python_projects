# Write a Python program to create a histogram from a given list of integers.
def histogram(items):
    for i in items:
        output = ""
        times = i
        while(times > 0):
            output += "@"
            times -= 1
        print(output)
histogram([1,2,3,4,5])

# Write a Python program to concatenate all elements in a list into
# a string and return it

def concentrate(items):
    output = ""
    for item in items:
        output +=  str(item)
    return output
print(concentrate(["s","z","y","m",1,2,3]))

# Write a Python program to print all even numbers from a given numbers list in
# the same order and stop the printing if any numbers that come after 237 in the
# sequence

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for number in numbers:
    if number == 237:
        print(number)
        break
    elif number %2 == 0:
        print(number)
        continue

# Write a Python program to print out a set containing all the colors from
# color_list_1 which are not present in color_list_2.


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))

# Write a Python program that will accept the base and height of a triangle
# and compute the area

def area(base, height):
    surface = (base * height) / 2
    return surface
print(area(10,5))
# Write a Python program to sum of three given integers. However,
# if two values are equal sum will be zero.

def sum1(a,b,c):
    suma = a + b + c
    if (a == b and c != a) or (a == c and b != a) or (b == c and a != b):
        suma = 0
    return suma
print(sum1(1,2,3))
print(sum1(1,1,1))
print(sum1(2,2,3))

# Write a Python program to sum of two given integers. However, if the sum
# is between 15 to 20 it will return 20.

def sum2(a,b):
    suma = a + b
    if suma in range(15,20):
        suma = 20
    return suma
print(sum2(10,7))
print(sum2(17,5))

# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

def sum3(a,b):
    if a == b or abs(a-b) == 5 or (a + b) ==5:
        return True
    else:
        return False
print(sum3(2,7))
print(sum3(2,3))
print(sum3(2,2))

# Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))

# Write a Python program to display your details like name, age, address in
# three different lines.

def personal_info():
    name, age = "Szymon", 19
    address = "Skawa, Rabka, Polska"
    print("Name: {}\nAge: {}\nAddress: {}\n".format(name, age, address))

personal_info()

# Write a Python program to solve (x + y) * (x + y).
x, y = 3,4
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2 = {}".format(x,y, result))

# Write a Python program to compute the distance between the points
# (x1, y1) and (x2, y2).

import math
p1 = [2,4]
p2 = [6,9]
distance = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[0])**2))
print(distance)

# Write a python program to get the path and name of the file that is currently executing.

import os
print("Current File Name : ",os.path.realpath(__file__))


# Write a python program to find the sum of the first n positive integers.

n = 8
suma = 0
for i in range(n+1):
   suma += i
print(suma)
