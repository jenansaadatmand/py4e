# Chapter 3 page 51 & 53 examples 
# Chained (if, elif, else) conditional versus nested (if, else (if, else)) conditional


x = 5
y = 10

# code in chained conditional 
 
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


# Code in nested conditional

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

 
    
# code is simplified using logical operators (and, or, not) 

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number')

print() 

# The print statement is excuted only if we make it past both conditionals in this nested conditional  
# We can get same effect if we used the logical boolean and operator

if 0 < x and x < 10:
    print('x is a single-digit number')

