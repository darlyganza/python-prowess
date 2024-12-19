import math
# firstName=input("Enter first name: ")
# lastName=input("Enter last name: ")
# fullName=lastName+" "+firstName
# print(fullName+ "\nWhat can I do for you today?")
# # expressions in python help to combine values together be it values in variables or not:
#
# # f strings: for formatted strings:
# year = "class 2C"
# print(f"{firstName} is my name and I study in {year}")

# using fstrings for formatting numbers:
mySalary = 355000
print(f"{mySalary:d}")
print(f"{mySalary:07d}")
print(f"{mySalary:d}")
print(f"{math.pi:f}")
print(f"{math.pi:4f}")
print(f"{math.pi:08.3f}")

month = 11
day = 312
year =2007
hour = 9
minute = 7
second =47
print(f"day: {day:d} year: {year} hour: {hour:2d}:{minute:02d}:{second:1d}")
# The 02.4f will help to format the number to the specific number of required size and the specified fixed numbers to
# go behind the point




