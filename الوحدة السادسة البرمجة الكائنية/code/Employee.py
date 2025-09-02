import datetime
from math import floor
from abc import ABC, abstractmethod

class Employee(ABC):

    total = 0
    __salary_raise = 1.1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.profile = None
        Employee.total += 1

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def _calculate_salary(self):
        pass

    @classmethod
    def from_string(cls, string):
        pass

