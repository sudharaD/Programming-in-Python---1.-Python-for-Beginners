from re import A


print(("Hi " + "Sudhara\n") * 3)

word = "a""b" # '' also work
print(word)

longString = "HiSudharaDhananjayaAbeythunga"

print(longString[3])
print(longString[2:10])
print(longString[-1])
print(longString[-2])
print(longString[-2:])
print(longString[:-2])

newString = 'Hello' + longString[2:]
print(newString)

a = "HI"
b = a
a = "Hello"
c = b

print(a + str(id(a)))
print(b + str(id(b)))
print(c + str(id(c)))

print(len(a))

print("H" in a)
print("e" not in b)

for i in range(3,2,-1): 
   print('!'*i)

for i in range(0,5):
    print(i)

x = "Computer Science and Engineering"
print (x[:3]+x[6]+x[9:12]+x[-11:-8])
