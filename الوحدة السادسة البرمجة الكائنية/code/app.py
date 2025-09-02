from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FreelancerProgrammer
from Roles import *
from Payment import *
from profile import Profile


if __name__ == '__main__':
    sara = FreelancerProgrammer('Sara', 'Mazin', 200, 5, 'PHP', ['Website', 'Blog'])

    print(sara.info())