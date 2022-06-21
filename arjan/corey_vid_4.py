""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=RSl87lqOXDE

Inheritance - creating subclasses.

Notes:

- See the change made to the Developer class (subclass of Employee) and the 
unique changes that it has

- isinstance() object is an instance of a class. 
- isinstance(mgr_1, Employee) --> True
- isinstance(mgr_1, Developer) --> False

Similarly,
- issubclass(Manager, Employee) -- True
- issubclass(Manager, Developer) -- False

For more examples look at the exception module for HTTPExceptions


When inheriting you can view the method resolution order by:
 `print(help(Developer))`

OUTPUT:

class Developer(Employee)
 |  Developer(first, last, pay)
 |  
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |  
 |  Methods inherited from Employee:
 |  
 |  __init__(self, first, last, pay)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  apply_raise(self)
 |  
 |  full_name(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |  
 |  raise_amount = 1.04

"""


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):  # these are all attributes to the class
        self.first = first  # equivalent to manually doing emp1.first = "Corey"
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):  # method = function within a class
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(
            first, last, pay
        )  # lets the employee class set the first few self attributes
        # Employee.__init__(self, first, last, pay) - equivalent but not as commonly used
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(
        self, first, last, pay, employees=None
    ):  # None because you don't want to pass mutable data types (list, dict, etc.)
        super().__init__(
            first, last, pay
        )  # lets the employee class set the first few self attributes

        # input of list of employees that the manager oversees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.full_name())


dev_1 = Developer("Corey", "Shafer", 50000, "python")
dev_2 = Developer("Test", "User", 60000, "java")

# manager test
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])


if __name__ == "__main__":
    print(dev_1.email)
    print(dev_2.email)
    print(dev_1.prog_lang)
    # print(help(Developer))
    # managers
    print(mgr_1.email)
    mgr_1.add_employee(dev_1)
    mgr_1.print_employees()
    mgr_1.add_employee(dev_2)
    mgr_1.print_employees()
