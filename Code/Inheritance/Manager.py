from Employee import Employee

class Manager(Employee):
    #attributes
    departament = ''
    
    #methods
    def __init__(self, name, age, salary, departament):
        super().__init__(name, age, salary)
        self.departament = departament
    
    #methods    
    def __str__(self):
        return f'Name: {self.name} -- Age: {self.age} -- Salary: ${self.salary} -- Departament: {self.departament}'