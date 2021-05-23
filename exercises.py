# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

def difference(x):
    if x <= 17:
        return 17 - x
    else:
        return (x - 17) * 2

print(difference(15))
print(difference(20))

# Write a Python program to test whether a number is within 100 of 1000 or 2000
def test(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)

print(test(950))
print(test(2070))
print(test(1500))

# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

def summ(x,y,z):
    if x == y == z:
        return 3 * (x + y + z)
    else:
        return x + y + z

print(summ(1,1,1))
print(summ(1,2,3))

def summ2(x,y,z):
    suma = x + y + z
    if x == y == z:
        suma = suma * 3
    return suma

print(summ2(1,1,1))
print(summ2(1,2,3))

# Write a Python program to get a new string from a given string where "Is"
# has been added to the front. If the given string already begins with "Is"
# then return the string unchanged.

def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str

print(new_string("IsArray"))
print(new_string("Moscow"))

# Write a Python program to get a string which is n (non-negative integer)
# copies of a given string.

def string_copies(str,n):
    result = ""
    for i in range(n):
        result = result + str
    return result

print(string_copies("abcd",3))

# Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

number = int(input("Whats your number: "))
mod = number % 2
if mod >= 0:
    print(f"{number} number is odd")
else:
    print(f"{number} number is even")

# Write a Python program to count the number 4 in a given list.
def fun(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    return count
print(fun([1,2,3,4,4,4,4,4]))
print(fun([4,4,4]))

# Write a Python program to get the n (non-negative integer) copies of the
# first 2 characters of a given string. Return the n copies of the whole string
# if the length is less than 2.

def copies(str,n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result
print(copies("abcd",4))
print(copies("a",5))

# Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(char):
    all_vowels = "aeiou"
    return char in all_vowels
print(is_vowel("c"))
print(is_vowel("e"))

# Write a Python program to check whether a specified value is
# contained in a group of values.

def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1,2,3,4,5,6,7],5))
print(is_group_member([1,2,3,4,5,6,7],8))
