# using classes insted of functions as decorators

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('display function ran')


@decorator_class
def display_info(name, age):
    print('display_info run with arguments ({}, {})'.format(name, age))



display_info('John', 25)
display()
