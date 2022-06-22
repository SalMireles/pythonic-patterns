""" Classes Practice using Corey videos: https://www.youtube.com/watch?v=jCzT9XFZ5bw

Property Decorators - Getters, Setters, and Deleters.

Notes:

Getter:

- When changing the first name of of instance the email will not update
unless you specifically update the email as well. How can we fix this?

You could make an email method, but now you have to go back and change all the email
attribute calls to method calls. OR you can add the property decorator (see email)


Setter:

- What if you wanted to set first and last name also when updating the full name?


"""


class Employee:
    def __init__(self, first, last, pay):  # these are all attributes to the class
        self.first = first  # equivalent to manually doing emp1.first = "Corey"
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def full_name(self):  # method = function within a class
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

    @full_name.deleter
    def full_name(self):
        self.first, self.last = None, None


if __name__ == "__main__":
    emp_1 = Employee("Corey", "Shafer", 50000)
    emp_1.full_name = "Corey Smells"
    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.full_name)
    # deleter example
    del emp_1.full_name
    print(emp_1.full_name)
