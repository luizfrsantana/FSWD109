from Employee import Employee
from Manager import Manager
from Executive import Executive
   
employee_1 = Employee('xpto', 35, 100.00)
manager_1 = Manager('qwe', 40, 2222.22, 'IT')
executive_1 = Executive('Bob', 50, 454515.25, 'CEO', 999999.99)

def breakline():
    print('-'*100)

breakline()    
print(employee_1)
print(manager_1)
print(executive_1)
breakline()
print(employee_1.totalSalary())
print(manager_1.totalSalary())
print(executive_1.totalSalary())

employee_1.setSalary(99999.00)
manager_1.setSalary(1000.00)
executive_1.setSalary(1.00)

breakline()
print(employee_1)
print(manager_1)
print(executive_1)
breakline()
print(employee_1.totalSalary())
print(manager_1.totalSalary())
print(executive_1.totalSalary())

        

        