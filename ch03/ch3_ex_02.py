# Exercise 2: 
# Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully
# by printing a message and exiting the program
# the following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input 


#Solution # 1:

sh = input("Enter Hours:") # sh = string hours
sr = input("Enter Rate:") # sr = string rate
try:
    fh = float(sh) # fh = float hours 
    fr = float(sr) # float rate
except:
    print("Error, please enter numeric input!")
    quit()
#print(fh, fr)
if fh > 40:
    print("Overtime")
    xp = (fh-40) * fr * 1.5 + 40*fr  # xp = pay
else: 
    print("Regular")
    xp = fh * fr  # xp = pay
print("Pay:", xp)




# Solution # 2:

try:
    hrs = float(input("Enter Hours:\n"))
    rate = float(input("Enter Rate:\n"))
except: 
    print("Error, please enter numeric input!")
    quit()
if hrs > 40:
    pay = (hrs-40)*rate*1.5 + 40*rate
else:
    pay = hrs*rate   
print("Pay:", pay)




