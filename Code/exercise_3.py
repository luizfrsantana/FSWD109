def breakLine():
    print("="*20)
    
#11. **String Interpolation:** Create a Python function named `format_string` that takes two parameters `name` and `age`. Use string interpolation to return a formatted string like "My name is [name] and I am [age] years old."

def format_string(name,age):
    return (f'My name is {name} and I am {age} years old')

print(format_string("Luiz",33))

breakLine()
# 12 **Dictionary Manipulation:** -  Write a Python code to remove the key-value pair where the key is 'age' from a dictionary `person`.
person = {'name':'Luiz','age':33,'city':'Rio'}
x = person.pop('age') #1-Option
print(person)
print(x)
del person['city'] #2-Option
print(person)

breakLine()
# 13  **Conditional with List:* - Given a list of numbers `numbers`, iterate through each number and print "Even" if it's even, and "Odd" if it's odd.
numbers = [1,2,3,3,5,6,7,8,9.9,11,11]
for number in numbers:
    if ((number%2)==0):print(f'Number #{number} is Even')
    else: print(f'Number #{number} is Odd')
breakLine()

# 14. **Loop with String:** -  Write a Python program that takes a string `word` as input and prints each character of the string along with its index.
string = 'word'
for value in range(len(string)):
    print(f'Index #{value} letter {string[value]}')
breakLine()
for index,character in enumerate(string):
    print(f'Index #{index} letter {character}')
breakLine()
   
#15. **Function with Variable Arguments:**
def average(*args):
    return sum(args) / len(args)

print(f'The average of 10, 20 and 30 is {average(10,20,30)}')
print(f'The average of 10, 10 and 10 is {average(10,10,10)}')
print(f'The average of 10, 20 and 30 is {average(5)}')
breakLine()

