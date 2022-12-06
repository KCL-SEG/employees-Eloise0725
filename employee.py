"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Salary:
    def __init__(self, wages, hour=1):
        self.wages = wages
        self.hour = hour

    def get_total(self):
        return self.wages * self.hour

    def __str__(self):
        if self.hour == 1:
            return f'monthly salary of {self.get_total()}'
        else:
            return f'contract of {self.hour} hours at {self.wages}/hour'


class Commission:
    def __init__(self, money, contract=1):
        self.money = money
        self.contract = contract

    def get_total(self):
        return self.money * self.contract

    def __str__(self):
        if self.contract == 1:
            return f'bonus commission of {self.get_total}'
        else:
            return f'commission of {self.contract} contract(s) at {self.money}/contract'


class Employee:
    def __init__(self, name, salary, commission=None):
        self.name = name
        self.salary = salary
        self.commission = commission

    def get_pay(self):
        if self.commission:
            return self.salary.get_total() + self.commission.get_total()
        else:
            return self.salary.get_total()

    def __str__(self):
        if self.commission:
            return f'{self.name} works on a {self.salary}. Their total pay is {self.get_pay()}.'
        else:
            return f'{self.name} works on a {self.salary} and receives a {self.commission}. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Salary(4000))

# Charlie works on a contract of 100 shours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Salary(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Salary(3000), Commission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Salary(25, 150), Commission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Salary(2000), Commission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Salary(30, 120), Commission(600))
