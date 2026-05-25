class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_details(self):
        print(self.name, self.__salary)

    def get_salary(self):
        return self.__salary


class Developer(Employee):

    def __init__(self, name, salary, tech):
        super().__init__(name, salary)

        self.tech = tech

    def show_tech(self):
        print(self.tech)


d = Developer("Gnani", 50000, "Python")

d.show_details()

d.show_tech()