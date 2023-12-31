# Chapter 3  Alternative conditional expression example on page 51
# Program to check if a number is divisible by 2, using modulus (%) operator 
# Prgram indicates if a number is an even number or an odd number

x = input("Enter Number:")
x = float(x)
if x%2 == 0: # use modulus % to check if number is divisible by 2 in a conditional if statement
    print("Number is even")
else:
    print("Number is odd")
