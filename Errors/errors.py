# SyntaxErrors
# print('Hello world)

# Runtime Errors: NameError, IndexError, TypeError, ValueError, ImportError

# Name Error - Access a variable that did not defined
# number = 10
# print(num)

# IndexError
# Raised when a sequance is refering which is out of sort_complex
# num_list = [1, 2, 3]
# print(num_list[10])

# Trpe Error
# strName = 'string' + 1
# print(strName)

# Value Error
# Occurs when a built-in operation or function receives an argument that has the right type but an invalid value
# print(int('hello'))

# Import/Modele not fount error
# import new_module

# try / except
num_input = input('Enter a number: ')

try:
    num_value = int(num_input)

# except NameError as ne:               we can use any number of exception to a single try
#     num_value = float(num_input)

except:
    num_value = -1

if num_value >= 0:
    print("Number entered")
else:
    print("Not a number")

print(type(3))
print(type(3.0))
print(int(3.0))