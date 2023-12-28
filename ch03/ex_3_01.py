# Exercise 3.1 on autograder:
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 
# and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program 
# (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.


# solution # 1
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    pay = (h-40)*r*1.5 + 40*r
else:
    pay = h*r
print("Pay:", pay)




#solution # 2:

hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hrs > 40:
    pay = (hrs-40)*rate*1.5 + 40*rate
else:
    pay = hrs * rate
print("Pay: ", pay)
