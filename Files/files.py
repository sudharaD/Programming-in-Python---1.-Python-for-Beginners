fhandle = open("myfile.txt")
# fcontents = fhandle.read()

# print(fcontents)

# if you want to print like that dont put fhandle.read to fcontents
# print(fhandle.read())

print(fhandle.readline())
print(fhandle.readline())
print(fhandle.readline())
print(fhandle.readline())
print(fhandle.readline())
print(fhandle.readline())

fh = open("myfile.txt", "w")

myString = "This line sending througf code editor\nHandle this"

fh.write(myString)

fh = open("Files/myfile.txt")

print(fh.read())

fhandle.close()
fh.close()
