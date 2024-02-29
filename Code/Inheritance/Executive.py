from Manager import Manager

class Executive(Manager):
    #attributes
    bonus = 0.00
    
    def __init__(self, name, age, salary, departament, bonus):
        super().__init__(name, age, salary, departament)
        self.bonus = bonus
    
    #methods    
    def __str__(self):
        return f'Name: {self.name} -- Age: {self.age} -- Salary: ${self.salary} -- Departament: {self.departament} -- Bonus: ${self.bonus}'
    
    def totalSalary(self):
        return super().totalSalary() + self.bonus