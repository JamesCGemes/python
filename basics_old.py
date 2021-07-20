# print(24 * 7)

# student_grades = [9.1, 8.8,7.5,9.1]

# gradesSum = sum(student_grades)
# gradesLength = len(student_grades)

# gradesMean = gradesSum / gradesLength

# print(max(student_grades))

# countGrades = student_grades.count(9.1)

# print(countGrades)

studentGrades = {"James" : 80.0, "Cassie" : 95.5}
#this shows the value of each item in a dict
print(studentGrades.values())
# this adds the values of each item in the dict
gradesSum = sum(studentGrades.values())

# print(gradesSum)

myNumbers = [30, 40, 50, 60, 70]

#adds new value to end of the list

myNumbers.append(80)

# print(myNumbers)

toClear = [10, 20, 30, 40]
#clears the items in a list
toClear.clear()

# print(toClear)

numbers = [1,2,3,4,5,6]
#returns the index of the item
# print(numbers.index(3))

# seconds = [1.2323442655, 1.4534345567, 1.023458894]
# current = 1.10001399445
#appends current to end of seconds
# seconds.append(current)

# print(seconds)

#remove 1.4534345567 from list
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]

monday_temperatures = [9.1, 8.8, 7.5]

monday_temperatures.append(8.5)

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
#append the first place of weekend to workdays
workdays.append(weekend[0])

print(workdays)

#get the first two index of workdays. 0:2 
print(workdays[0:2])








