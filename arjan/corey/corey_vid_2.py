""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=BJ-VvGyQxho

Class Variables.

Notes:
- Have same class variables for all instances. 
- What kind of data should be shared amongst all employees?
- Example: raise for all employees

- instance checks for attribute. If none found then it looks for attribute from
the class then any inherited class. 

- self.<attribute> allows this to be overwritten by the class AND by a particular 
instance AND any subclass that inherits. This is good flexibility but when can it be 
too much?

- number of employees is an example of a quantity that you would want to fix
and be the same for all instances so don't use self.

"""


class Employee:

    num_of_employees = 0

    raise_amount = 1.04

    def __init__(self, first, last, pay):  # these are all attributes to the class
        self.first = first  # equivalent to manually doing emp1.first = "Corey"
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_employees += 1

    def full_name(self):  # method = function within a class
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


if __name__ == "__main__":
    # setup
    emp_1 = Employee("Corey", "Shafer", 50000)
    emp_2 = Employee("Test", "User", 60000)

    print(emp_1.pay)
    print(emp_1.apply_raise())
    print(Employee.num_of_employees)
    # view namespace of instance or Class
    print(emp_1.__dict__)
    print("---------------")
    print(Employee.__dict__)
