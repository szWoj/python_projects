# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
import random


def get_random_list():
    size = input("What size of random list you want? ")
    l = [random.randint(1,100) for _ in range(int(size)) ]
    return l
    

def shorter(lst):
    new_list = [lst[0], lst[-1]]
    return new_list

random_list = get_random_list()
first_last_list = shorter(random_list)

print(random_list)
print(first_last_list)

# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.

def no_duplicants(lst):
    sets_of_elements = set(lst)
    back_to_list = list(sets_of_elements)
    return back_to_list

print(no_duplicants([1,2,3,4,1,2,3,4]))

def no_duplicants2(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
print(no_duplicants2([1,2,3,4,5,1,2,3,4,5]))

# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, except with
# the words in backwards order.

def get_a_string():
    your_string = str(input("What's your string/sentence? "))
    return your_string.split(" ")

def convert_list_to_string(lst, seperator = " "):
    return seperator.join(lst)

new_sentence = get_a_string()
print(new_sentence)
new_sentence.reverse()
print(new_sentence)
the_right_sentence = convert_list_to_string(new_sentence, seperator = " ")
print(the_right_sentence)

