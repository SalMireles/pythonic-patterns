""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=rq8cL2XMM5M

Class Methods and Static Methods.

Notes:
- Regular methods: take instance as first arguement
- Static methods: Don't take any arguements as defaults and behave like regular functions
- Class methods: take class as first arguement using @classmethod

Employee.set_raise_amount(1.05) equivalent to Employee.raise_amount = 1.05,
but we now use a class method.

Side note: Can create an "alternative constructor" meaning a custom way to pass
in data to the class by using a class method.

- The datetime module has really good examples of this usage such as "fromtimestamp"

- Use static methods when you don't need to use the instance (self) or class (cls). 
Regular function with some logic that relates to the class


"""

import datetime


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):
        # Construct an employee from a string formatted as such: "Steve-Smith-30000"
        first, last, pay = employee_string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == "__main__":
    # setup
    emp_1 = Employee("Corey", "Shafer", 50000)
    emp_2 = Employee("Test", "User", 60000)
    Employee.set_raise_amount(1.05)

    # alterantive constructor usage example
    emp_3_string = "Steve-Smith-30000"
    emp_3 = Employee.from_string(emp_3_string)

    # example of using the static method
    my_date = datetime.date(2017, 7, 10)

    print(Employee.is_workday(my_date))
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print(Employee.raise_amount)
    print(emp_3)
