

class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@gmail.com'
        Employee.num_of_emp += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod #class method works with class,
                #changes class instances for all artibutes
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
    def __repr__(self): #represents how the object will be printed to the user
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self): # also represents how the object will be printed to the user.
        return '{} - {}'.format(self.fullname(), self.email) # gets priority over __repr__

    def __add__(self, other): #explains to the program what do we mean if we want to add two employees
        return self.pay + other.pay # in this case we want to add theis pay

    def __len__(self): #explains to the program what we mean by calling len() function on the object
        return len(self.fullname()) - 1
        


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang








class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('---->', emp.fullname())








emp_1 = Employee("simon", "wojdi", 40000)
emp_2 = Employee("sebastian", "wojdyyy", 50000)

dev_1 = Developer("simon", "wojdi", 40000, 'Python')
dev_2 = Developer("sebastian", "wojdyyy", 50000, 'JAVA')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])
mgr_1.add_emp(emp_1)
mgr_1.remove_emp(dev_1)



print(emp_1)
print(dev_2)

print(1 + 2)
print(int.__add__(1, 2))
print(str.__add__('2', '2'))

print("Sum of two employees salaries: ", mgr_1 + dev_1)

print(len('test'))
print('tests'.__len__())

print(len(mgr_1))
##print(repr(emp_1))
##print(str(emp_1))
##
##print(emp_1.__repr__())
##print(emp_1.__str__())
##print(dev_1.email)
##
##print(dev_2.prog_lang)
##
##print(mgr_1.email)
##mgr_1.print_emp()
##
##print(isinstance(mgr_1, Manager))
##print(issubclass(Manager, Developer))
##emp_5 = Employee("simon", "wojdi", 40000)
##emp_4 = Employee("sebastian", "wojdyyy", 50000)
##
##emp_str1 = 'John-Doe-7000'
##emp_str2 = 'Steve-Smith-3000'
##emp_str3 = 'Jane-Doe-90000'
##
##import datetime
##my_date = datetime.date(2021, 5, 15)
##print(Employee.is_workday(my_date))
##
##
##
##
##new_emp_1 = Employee.from_string(emp_str1)
##new_emp_2 = Employee.from_string(emp_str2)
##new_emp_3 = Employee.from_string(emp_str3)
##print(new_emp_1.email)
##print(new_emp_2.last)
##print(new_emp_3.pay)






