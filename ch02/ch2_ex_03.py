# Exercise 3: write a program to prompt the user for hours and rate per hour to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25) 
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# You should use input to read a string and float() to convert the string to a number.
# do not worry about error checking or bad user data.

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print("pay:", hrs * rate)

