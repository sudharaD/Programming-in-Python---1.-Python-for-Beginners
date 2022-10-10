import keyword

a = "abc" + 'xyz'
print(a)
print(type(a))
type(a)
b = 64;
print(type(b))
print(type(64.0))
c = 10 > 5
print(type(c))
d = 2 + 3j
print(type(d))

x = 88
y = x
print(y)
print(id(x))
print(id(y))
x = 89
print(id(x))
print(id(y))
print(x)
print(y)
print(id(a))
b = a
print(id(b))
print(a[2])

print(keyword.kwlist)

var = 100
print(type(var))
var = 'sd'
print(type(var))

strWeight = "55"
intWeight = strWeight + str(5)
print(intWeight)
print(5 + int(strWeight))
age = 20
print(age)
