from Employee import Employee

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        if employees is None:
            employees = []
        self.employees = employees

    def info(self):
        return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}; Salary: {self.__salary}; Employees: {len(self.employees)}'

    def _calculate_salary(self):
        return self.__salary

    def from_string(cls, string):
        pass