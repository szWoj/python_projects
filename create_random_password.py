import random


def password(characters):
    
    special_character = ['!','@','#','$','%','^','&','*',',',".","/"]
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase = [x.upper() for x in lowercase]
    d = special_character + lowercase + uppercase

    random.shuffle(d)


    ran = random.choices(d, k = characters)
    ran = "".join(ran)
    return print(ran)

password(10)
