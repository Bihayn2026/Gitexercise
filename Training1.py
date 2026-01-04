
First_name = input("Enter First_name")
Last_name = input("Enter Last_name")
Name = f" How are you doing today {First_name} {Last_name}"  
print(Name)

Music = ("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
print(Music)	

import sys
print(sys.version)

import datetime
now = datetime.datetime.now()
print("Current Date and Time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# area of a circle

import math
from math import pi
r = float(input("Enter radius of a circle"))
area_circle = pi*r**2
print(area_circle)


Lname = input("Enter Lname")
Fname = input("Enter Fname")
print(Lname + " " + Fname)
Full_name = f"{Lname} {Fname}"
print(Full_name)

#List and Tuple Generator
#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

Num = input("Enter Number: ")
list = Num.split(",")
tuple = tuple(list)
print("List: ",list)
print("Tuple: ",tuple)

# File Extension Extractor
#Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename: abc.java

# file_name = input("Enter File name")
# file_exten = file_name.split(".")
# print(file_exten[-1])

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
print("%s %s" % (color_list[0], color_list[3]))

#9. Exam Schedule Formatter
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

print (f"The examination will start from : %i/%i/%i" % exam_st_date)

#10. Number Expansion Calculator
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
# Expected Result : 615

a= int(input("Enter the Number"))
n1 = int("%s" % (a))
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)

#11. Function Documentation Printer

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

Number = float(input("Enter the Number: "))
print("Expected Result: ", (abs(Number)))

print(abs.__doc__)
print(sorted.__doc__)

#12. Monthly Calendar Display

# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

import calendar
y = int(input("Enter the Year: "))
m = int(input("Enter the Month: "))
print(calendar.month(y,m))

#13. Multi-line Here Document
# Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

#Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

date1 = datetime.datetime(2014, 7, 2)
date2 = datetime.datetime(2014, 7, 11)
difference = date2-date1
print("Expected Output: ", difference.days,"days")

from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

print("Expected Output:", (date2 - date1).days, "days")


#15. Sphere Volume Calculator

#Write a Python program to get the volume of a sphere with radius six.

import math
r = 6
area = math.pi*(r**2)
print(area)

#16. Difference from 17

#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, 
# return twice the absolute difference.

def difference(n):
    if n > 17: 
        return 2*(abs(n - 17))
    else:
        return abs(n - 17)
print(difference(22))