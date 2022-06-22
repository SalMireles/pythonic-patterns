""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=3ohzBxoFHAY

Special (Magic/Dunder) Methods.

Notes:

- Special methods to use within classes
- changes how objects are printed or displayed
- Format outputs using dunder methods
- if no str dunder the repr dunder is used as fallback

__len__ and __add__ are other examples of behavior that objects run when running
len() or simply print (1 + 2)

See the difference:

<__main__.Employee object at 0x103497d30>

vs

Employee('Corey', 'Shafer', '50000')



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

    def __repr__(self):  # mainly used for debugging
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):  # readable output
        return f"{self.full_name()} - {self.email}"


if __name__ == "__main__":
    emp_1 = Employee("Corey", "Shafer", 50000)
    emp_2 = Employee("Test", "User", 60000)
    print(emp_1)  # defaults to printing str dunder
    print(repr(emp_1))  # or print(emp_1.__repr__())
    print(str(emp_1))
    print(emp_1.apply_raise())
