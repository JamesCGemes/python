myfile = open('fruits.txt')

# print(myfile.read())

#better way to open and read a file

with open("fruits.txt") as myfile:
    content = myfile.read()


print(content)    


