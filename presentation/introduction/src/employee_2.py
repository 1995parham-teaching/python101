import abc


class Employee(abc.ABC):
    """
    common abstract base class for all employees.
    """

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    @abc.abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return (
            f"({type(self).__name__}): {self.name} ${self.salary} {id(self)}"
        )


class FullTimeEmployee(Employee):
    def __init__(self, name: str):
        super().__init__(name, 1000)

    def __str__(self):
        return f"Name : {self.name}, Salary: ${self.salary} for working full time during a month"


class PartTimeEmployee(Employee):
    def __init__(self, name: str, hours: int):
        super().__init__(name, hours * 40)
        self.hours = hours

    def __str__(self):
        return f"Name : {self.name}, Salary: ${self.salary} for {self.hours} hours of working during a month"


if __name__ == "__main__":
    emp1 = FullTimeEmployee("Parham Alvani")
    emp2 = PartTimeEmployee("Elahe Dastan", 40)

    print(emp1)
    print(emp2)
