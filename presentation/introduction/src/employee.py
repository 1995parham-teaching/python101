class Employee:
    """
    common base class for all employees
    """

    employee_count = 0

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_count(self):
        print(f"Total Employee {Employee.employee_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


if __name__ == "__main__":
    emp1 = Employee("Zara", 2000)
    emp1.display_count()
    emp1.name
