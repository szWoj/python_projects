# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str)-2):
        if str[i:i+3] == "cat":
            count_cat +=1
        if str[i:i+3] == "dog":
            count_dog += 1
    if count_cat == count_dog:
        return True
    return False

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))


stri = "Szymon"
for i in range(len(stri)):
    print(i)

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    count = 0
    for i in range(len(str) -3):
        if str[i:i+4] in ["code","coqe","cowe","coee","core","cote","coye","coue","coie","cooe","cope","coae","cose","cofe","coge","cohe","coje","coke","cole","coze","coxe","coce","cove","cobe","cone","come"]:
            count+=1
    return count
print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cokecowedkslcode')) 
