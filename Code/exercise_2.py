def breakLine():
    print("="*20)

#question 6 - Given a string `sentence`, extract the first five characters and print them.
string = "Rodrigues"
print(f'First five characters os the string {string} is {string[:5]}')
breakLine()

#question 7 - Perform the following operations on a list `numbers`: Append the number '10' - Remove the number '5' - Print the final list.
numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(10)
numbers.remove(5)
print(f'List: {numbers}')
breakLine()

#question 8 - Dictionary `person` with keys 'name', 'age', and 'city'. Print all the key-value pairs using a loop.
person = {'name':'Luiz','age':33,'city':'Rio'}
for attribute in person.keys():
    print(f'Attribute is {attribute} value is {person[attribute]}')
breakLine()
    
#question 9 - Check if the variable `num` is greater than 10. If it is, print "Greater than 10"; otherwise, print "Less than or equal to 10".
num = 7
if num > 10: print("Greater than 10")
else: print('Less than or equal to 10') 
breakLine()

#question 10 -  Write a Python function named `greet` that takes a parameter `name` with a default value of "Guest". The function should print "Hello, [name]!" where [name] is replaced with the value passed or the default value if none is provided.

def greet(name='Guest'):
    print(f'Hello {name}')
    
greet('Luiz Felipe')
