from Employee import Employee
from Roles import *
from Payment import *


class Programmer(Employee, ProgrammerRole, Salary):
    def __init__(self, first_name, last_name, salary, lang, projects=None):
        Employee.__init__(self, first_name, last_name)
        ProgrammerRole.__init__(self, lang, projects)
        Salary.__init__(self, salary)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}; Salary: {self.__salary}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    def from_string(cls, string):
        pass

    def assign_project(self, project):
        self.projects.append(project)


class FreelancerProgrammer(Employee, ProgrammerRole, HourlyPayment):
    def __init__(self, first_name, last_name, hour_rate, work_hours, lang, projects=None):
       Employee.__init__(self, first_name, last_name)
       HourlyPayment.__init__(self, hour_rate, work_hours)
       ProgrammerRole.__init__(self, lang, projects)
       if projects is None:
           projects = []

    def info(self):
        return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}; Salary: {HourlyPayment.calculate_salary(self)}'

    def _calculate_salary(self):
        return HourlyPayment.calculate_salary(self)
