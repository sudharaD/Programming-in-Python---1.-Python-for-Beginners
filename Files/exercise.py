fhandle1 = open("file1.txt")

line1 = fhandle1.readline()
line2 = fhandle1.readline()

fhandle1.close()

print(line1 + line2)

fhandle2 = open("file2.txt", "w")

myString = (line1 + line2)

fhandle2.write(myString)

fhandle2.close()

fhandle3 = open("file2.txt")

print(fhandle3.read())