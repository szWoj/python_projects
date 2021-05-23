class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property #by adding @property we can access fullname as an atribute
    def fullname(self): # no () needed below while calling it 
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first.lower(), self.last.lower())

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
    
emp_1 = Employee('Mark', 'Robson')

emp_1.first = 'Jim'



emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
