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


studentGrades = {"James" : 80.0, "Cassie" : 95.5, "Lee" :100}


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:    
        the_mean = sum(value) / len(value)
    return the_mean

    
print(mean(studentGrades))    

