""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=3ohzBxoFHAY

Special (Magic/Dunder) Methods.

Notes:

- Special methods to use within classes

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
