# Exercise 3.3: write a program to prompt for a score between 0.0 and 1.0
# If the score is out of range, print an error message
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score     Grade
# >= 0.9    A
# >= 0.8    B
# >= 0.7    C
# >= 0.6    D
# < 0.6     F


# Enter score: 0.95
# A

# Enter score: perfect
# Bad score

# Enter score: 10.0
# Bad score

# Enter score: 0.75
# C

# Enter score: 0.5
# F

# Run the program repeatedly as shown 
# to test the various different values for input


# If the user enters a value out of range, 
# Print a suitable error message and exit. For the test, enter a score of 0.85.
# Desired output B, enter 0.8

try:
    grade = float(input("Enter Score: "))
except:
    print("Bad score")
    quit()  
        
if grade < 0.0 or grade > 1.0:
    print("Score is out of range!")
elif grade >= 0.9: 
    print("A" )
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C") 
elif grade >= 0.6:
    print("D")   
else:
    print("F") 


# solution for autograder on website: 
    
# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, 
# print a grade using the following table:
#Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, 
# print a suitable error message and exit. 
# For the test, enter a score of 0.85.   
# desired output is B 
         

score = input("Enter Score: ")
score = float(score)
if score < 0 or score > 1.0:
    print("Score is out of range!")
    quit()
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F") 
    
