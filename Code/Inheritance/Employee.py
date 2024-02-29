class Employee():
    
    #attributes
    name = ''
    age = 0
    salary = 0.00
    
    #methods
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f'Name: {self.name} -- Age: {self.age} -- Salary: ${self.salary}'
    
    def totalSalary(self):
        return self.salary
    
    def setSalary(self,salary):
        self.salary=salary