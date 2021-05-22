import random
a = [random.randint(1, 100) for i in range(20)]
b = [random.randint(1, 100) for i in range(15)]



lst = []

for i in a:
    if i in b:
        lst.append(i)


print(list(set(lst)))





a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in a:
    if i in b:
        c.append(i)
        
print(list(c))


num = [2,6,9,0,5,3,4,6,11,22,33,44,55]

num1 = [number for number in num if number % 2 == 0]

print(num1)
