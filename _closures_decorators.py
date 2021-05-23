
#closures
def outer_function(msg):
    message = msg #free variable

    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')

bye_func = outer_function('Bye')

hi_func()
bye_func()







# decorator -function taking another function as an argument,
# modifying it a lil, and returns it

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

#decorated_display = decorator_function(display)
#decorated_display()
display()



