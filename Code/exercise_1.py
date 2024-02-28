#Question 1 - Python code to assign values 1,4 and 3 to a,bcc in a single line.
a,b,c = 1,4,3
print(a,b,c)

#Question 2 - Length of a given string
string = 'Text'
print(f'Length of {string} is {len(string)}')

#Question 3 - Add the element 'apple' to the end of a list  'fruits'
fruits = ['orange','banana','grape']
print(f'List of fruits without "apple": {fruits}')
fruits.append('apple')
print(f'List of fruits with "apple" added: {fruits}')

#Question 4 - Code to find the number os key-value pairs in a dictionary
my_dict = {'name':'Luiz','age':33,'ID':123}
number_of_pairs = len(my_dict)
print(f"The number of key-value pairs in the dictionary is: {number_of_pairs}")

#Question 5 - Gloval variable "x" outside a function and a local variable "x". Print both

x = 'GLOBAL'
def my_func():
    x = 'LOCAL'
    print(x)
    
def my_func_global():
    global x
    x = 'LOCAL'
    print(x)
    
print(f'I am {x}')
my_func()
print(f'I am {x}')
my_func_global()
print(f'I am {x}')


print(x)

    
