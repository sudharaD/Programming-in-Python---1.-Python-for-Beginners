import math

print(min(5, 10))
print(max(5, 10))

# def functionname(parameters):
#     "function_docstring"
#     function_suit
#     return[expression]

def printme(str):
    "Put a text message to the screen"
    print(str)
    return

# exercise 1
def greet(name):
    "Greet a person with name"
    print("Hello!", name)
    return

greet(input("What is your name? : "))

greet("Kamal")
greet("Nimal")
greet("Palitha")

def circumference(r):
    circumference = 2 * math.pi * r
    print("Circumference is", circumference)
    return

def area(r):
    area = math.pi * r * r
    print("Area is", area)
    return

r = int(input("Enter the radius: "))

circumference(r)
area(r)

# Type Error
# def greet(name, msg):
#     print("Hello", name + ', ' + msg)   

# greet("Jane")

def my_function(*kids):
 print("The youngest child is " + kids[2])
my_function("Ajay", "Vijay", "Sanjay") 

# Important
def add(a, b):
    return a+5, b+5
print(add(3, 2))

def greet(name, msg="Good morning!"):  
    print("Hello", name + ', ' + msg) 

greet("Monica")

def greet(*names):
    for name in names:
             print("Hello", name)

greet("Jane", "Monica", "Joe", "Andrew")

def factorial(number):
    if number <= 1: return 1
    return number * factorial( number-1 )

print(factorial(5))

def greet(name, msg):
    print("Hello", name + ', ' + msg) 

greet("Jane")

