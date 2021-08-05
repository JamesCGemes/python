


myfile = open('fruits.txt')

# print(myfile.read())

#better way to open and read a file

with open("fruits.txt") as myfile:
    content = myfile.read()


print(content)   

with open("test/veggies.txt", "w") as veggie_names:
    veggie_names.write("tomato")
    veggie_names.write("\ncucumber")

    


# with open("fruits.txt") as fruit_file:
#     content = fruit_file
    
    
# print(content[:10]) 

def how_many(character, path):
    with open(path) as file_to_read:
        content

