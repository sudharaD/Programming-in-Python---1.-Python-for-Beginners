def get_input():

    integer_value = get_input.input("Please enter a number: ", 'int')
    print(integer_value)


x = input("Enter:\n")
print(type(x))
x = int(x)
print(type(x))
y = int(input("Enter:\n"))
print(type(y))

# print several variables inline
print(1, 2, 3, 4)

# change default seperator
print(1, 2, 3, 4, sep="*", end='#\n')

# {} as a placeholser
print("value of 'a' is {} and value of 'b' is {}".format(1,2))

# can specify the order
print("value of 'a' is {1} and value of 'b' is {0}".format(1,2))

a = input("Enter number 1: ")
b = input("Enter number 2: ") 
print(a+b)

print("Where", "are", "the", "spaces")


