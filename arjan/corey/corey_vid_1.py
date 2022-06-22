""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=ZDa-Z5JzLYM

Classes and Instances.

"""


class Employee:
    def __init__(self, first, last, pay):  # these are all attributes to the class
        self.first = first  # equivalent to manually doing emp1.first = "Corey"
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):  # method = function within a class
        return f"{self.first} {self.last}"


if __name__ == "__main__":
    # setup
    emp_1 = Employee("Corey", "Shafer", 50000)
    emp_2 = Employee("Test", "User", 60000)

    print(emp_1.email)
    print(emp_2.full_name())
    print(
        Employee.full_name(emp_2)
    )  # equivalent to above - self gets passed in in the background
