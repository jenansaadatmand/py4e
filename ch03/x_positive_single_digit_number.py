# A program to test if x or a number is between 0 and 10
# The number is positive, x > 0 or x < 0 ; and single_digit, x < 10 


x = 11
if 0 <= x:
    if x < 10:
        print('x is a positive single-digit number')
    elif x == 0:
        print('x is equal to 0')
    elif x >10:
        print('x is larger than 10')
else: 
        print('x is a negative number')    

print()

# We can get the same effect of this nested conditional if statement in if statement 
# By using the logical boolean and operator
        
if 0 <= x and x <= 10:
     print('x is a positive single_digit number')
else:
     print('x is larger than ten or smaller than 0')
