values = [15, 20, 96, 32, 17]
print(values)
print(values[0])
print(values[0:3])
values[4] = 100
values.append(60)
print(values)
values.remove(100)
print(values)
values.remove(values[0])
print(values)
del values[0]
print(values)

list = ['ph', 'ch', 1997, 2000, 2000, 2009]
list[2] = 2001
list.remove(2000)
list.append(2015)


# print : [2001, 2000, 2009, 2015]
print(list[2:])

data = [[1,1,1], [2.1,2.2,2.3], [3,3,3]]
print(data[1] [1])
data [1] [1] = 25
print(data)
data[1].append(2)
print(data)

print(len(values))
print(len(list))
print(len(data))
print(len([1,2,3]))

a = [1,2,3]
b = [4,5,6]

print(a+b)

print(['Hi'] * 5)
print(a * 3)

print(3 in [1,2,3])
print(5000 in list)
print(2000 in list)

for x in [1,2,3]:
    print(x)
for i in list:
    print(i)
    print(x)

# Indexing
print(list)
print(list[2])
print(list[-4])

# Slicing
print(list[3:])
print(list[-3:])

y = 2000
list.remove(y)
print(list)

# Exercise
numList = [2,4,6,8,3,4,2,1]
evenNumList = []

for x in numList:
    if x % 2 < 1:
        evenNumList.append(x)

for x in evenNumList:
    firstNumber = x
    evenNumList.remove(x)
    if x not in evenNumList:
        evenNumList.insert(0, x)

print(evenNumList)
evenNumList.reverse()
print(evenNumList)

numList2 = [2,4,6,8,3,4,2,1]
evenNumList2 = []

for i in numList2:
    if (i%2==0) and (i not in evenNumList2):
        evenNumList2.append(i)

print(evenNumList2)


