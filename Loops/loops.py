for counter in [1, 2, 3, 4, 5]:
    # print("This is a print value: " + str(counter))
    print("This is a print value: ", counter)

print("-----------------------------------------------")

for counter in list(range(10)):
    print("This is a print value: ", counter)

print("-----------------------------------------------")

for counter in list(range(5, 10)):
    print("This is a print value: ", counter)

print("-----------------------------------------------")

for counter in list(range(0, 10, 3)):
    print("This is a print value: ", counter)

print("-----------------------------------------------")

for counter in list(range(-10, -100, -30)):
    print("This is a print value: ", counter)

print("-----------------------------------------------")

# Exercise 1
sum = 0
for number in list(range(101)):
    if (number % 2) == 0:
        sum += number

print(sum)

sum2 = 0
for number2 in list(range(0, 101, 2)):
    sum2 += number2
print(sum2)

repeatNumber = int(input("Enter the repeat count: "))
while(repeatNumber != 0):
    if (repeatNumber < 0):
        repeatNumber *= -1
    print("Repeated number: ", repeatNumber)
    repeatNumber -= 1;
print("End")

# Exercise 2
horizontalCount = 0
while horizontalCount < 5:
    verticalCount = 0
    while verticalCount < 10:
        print("$", end = '')
        verticalCount += 1;
    print("")
    horizontalCount += 1;

# Example
n = 10
for i in range(0, 10):
    print(i, "Hello")
    if (i == 3):
        print("Count Aboard")
        break
    print(i, "World!")

# Example
for i in range(-2, 3):
    if i == 0:
        continue
    print("5 /", i, " = ", (5.0 / i))

# pass keyword
list = [1, 2, 3, 4, 5]
for x in list:
    pass
print("End")

# example
numbers = [1, 32, 4, 2, 32, 5, 2]
for number in numbers:
    print("Looking at ", number)
    if number == 5:
        print("Number found")
        break
else:
    print("Number not found")

print("End")

print(3/2)
    