
import time
import os
import pandas


# myfile = open('fruits.txt')

# print(myfile.read())

#better way to open and read a file

# with open("fruits.txt") as myfile:
#     content = myfile.read()


# print(content)   

# with open("test/veggies.txt", "w") as veggie_names:
#     veggie_names.write("tomato")
#     veggie_names.write("\ncucumber")

    


# with open("fruits.txt") as fruit_file:
#     content = fruit_file
    
    
# print(content[:10]) 

# def how_many(character, path = "veggies.txt"):
#     with open(path) as file_to_read:
#         content = file_to_read()
#         return content.count(character)




# def how_many(character, path = "veggies.txt"):
#     file = open(path)
#     content = file.read()
#     return content.count(character)

# print(how_many("cucumber"))    



# print(how_many("cucumber"))



# with open("file.txt", "w") as write_to:
#     write_to.write("snail")

# with open("bear.txt") as file:
#     contents = file.read()


# with open("first.txt", "w") as file:
#     file.write(contents[:90])            

# with open("fruits.txt", "a") as myfile:
#     myfile.write("\nstrawberry")

# with open("fruits.txt", "r") as read_file:
#     contents = read_file.read()

# with open("veggies.txt", "a") as append_to:
#     append_to.write(contents)    

# with open("data.txt", "a+") as append_file:
#     append_file.seek(0)
#     content = append_file.read()
#     # append_file.seek(0)
#     append_file.write(content)
#     append_file.write(content)

# while True:
#     if os.path.exists("test/veggies.txt"):

#         with open("test/veggies.txt") as file:
#             print(file.read())
            
#     else:
#         print("File not found")
#     time.sleep(5)


while True:
    if os.path.exists("test/temps_today.csv"):
        data = pandas.read_csv("test/temps_today.csv")
        print(data.mean())
            
    else:
        print("File not found")
    time.sleep(5)