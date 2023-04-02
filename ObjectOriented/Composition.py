
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay*12) + (2*self.bonus)


class Employee:
    def __init__(self,name,pay,bonus):
        self.name = 'Ruhul'
        self.obj_salary = Salary(pay,bonus)

    def totalCost(self):
        return self.obj_salary.annualSalary()

emp1 = Employee('Ruhul',12,10)
print(emp1.totalCost())