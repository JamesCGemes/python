day_hours = 24
week_days = 7
week_hours = day_hours * week_days
#print("there are" , week_hours, " hours in a week")

# studentGrades = {"James" : 80.0, "Cassie" : 95.5, "Lee" :100}

# #print(studentGrades["Cassie"])

# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

    
# print(mean([1,4,5]))    


#function that calculates area of a square with even sides
def area_of_square(l):
    area_of = l * l
    return area_of


 #convert fluid ounce to milli   
def f_to_m(input):
    milli = 29.57353
    convert_to = input * milli
    return convert_to   

#print(f_to_m(5))    


# studentGrades = {"James" : 80.0, "Cassie" : 95.5, "Lee" :100}

#below will take a list or dict
def mean(value):
    #this checks for the type of the input dict vs list
    #if type(value) == dict:
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:    
        the_mean = sum(value) / len(value)
    return the_mean

    
#print(mean(studentGrades))    

#function that prints true if string has more than eight characters or false if it has less.

def has_eight(input):
    if len(input) < 8:
        return False
    elif len(input) >= 8:
        return True    

#print(has_eight("jamesgemes"))

def temp(input):
    if input <= 7:
        return "Cold"
    else:
        return "Warm"    

#print(temp(7))

def which_temp(input):
    if input in range(15, 26):
        return "Warm"
    elif input < 15:
        return "Cold"
    else:
        return "Hot"    


#print(which_temp(-5))            

#take user input for which_temp
#user_input = float(input("Please enter the temperature:"))
#print(which_temp(user_input))

#take user input of name and return a hello + name
#user_name = input("Whats your name?")
#below works in python 2 and 3
#message = "Hello %s!" % user_name
#below works in python 3.6 and up.
#new_message = f"Hello {user_name}!"
#print(new_message)

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")

#message_03 = "Hello %s %s!" % (name, surname)

# message_04 = f"Hello {name} {surname}"

#print(message_03)
# print(message_04)

# if name == "james" and surname == "gemes":
#     print( "your awesome!")


# def say_hi(i):
#     return "Hi %s" % i

# def say_hello(i):
#     return "Hi %s" % i.title()


# print(say_hello("james"))

# monday_temps = [9.1, 8.8, 7.6]

# for temp in monday_temps:
#     print(round(temp))

colors = [11, 34, 98, 43, 45, 54, 54.3]
#loops throug color and prints only if over 50
# for color in colors:
#     if color > 50:
#         print(color)

# for color in colors:
#     if type(color) == int and color > 50:
#         print(color)

studentGrades = {"James" : 80.0, "Cassie" : 95.5, "Lee" :100}
# itterate through a dictionary
# for grade in studentGrades.items():
#     print(grade)

# for grades in studentGrades.values():
#     print(grades)

# for grades in studentGrades.keys():
#     print(grades)

# for key, value in studentGrades.items():
#     print("{} has a grade of {}" .format(key, value))


    
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

# for persons_name, persons_number in phone_numbers.items():
#     print("{}: {}" .format(persons_name, persons_number))


# for persons_number in phone_numbers.values():
#     print(persons_number.replace("+", "00"))


# a = 0
# while a < 5:
#     a = a + 1
#     print(a)    


# while True:
#     username = input("Please enter your username:")
#     if username == 'James':
#         break
#     else:
#         print("Sorry wrong name try again")
#         continue


temps = [221, 234, 430, 230]

#easier version of a for loop for new list.
new_temps = [temp / 10 for temp in temps]

#if you need to use an if else in a list comprehension the "for" "in" portion goes after the if else.
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

# print(new_temps)

def only_integers(lst):
    return [i for i in lst if isinstance(i, int)]

# print(only_integers([1,2,3,"cow"]))

def more_than_zero(lst):
    return [i for i in lst if i > 0]

# print(more_than_zero[1,-0,100,-50])    

def zeros(lst):
    return [i in lst if not isinstance(i, str) else 0 for i in lst ]
