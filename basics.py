day_hours = 24
week_days = 7
week_hours = day_hours * week_days
#print("there are" , week_hours, " hours in a week")

studentGrades = {"James" : 80.0, "Cassie" : 95.5, "Lee" :100}

#print(studentGrades["Cassie"])

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

    
print(mean([1,4,5]))    