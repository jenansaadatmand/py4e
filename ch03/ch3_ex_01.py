# Exercise 1: Rewrite exercise ex_2_3.py, pay computation 
# To give the employee 1.5 times the hourly rate for hours worked above 40 hours
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# Solution # 1
sh = input("Enter Hours:") # sh = string hours
sr = input("Enter Rate:") # sr = string rate
fh = float(sh) # fh = float hours 
fr = float(sr) # float rate
if fh > 40:
    print("Overtime")
    xp = (fh-40) * fr * 1.5 + 40*fr  # xp = pay
else: 
    print("Regular")
    xp = fh * fr  # xp = pay
print("Pay:", xp)


# solution # 2 autograder
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    reg = (h*r)
    otp = (h-40)* r*0.5
    xp = reg + otp
else:
    xp = h*r
print("Pay:", xp)


# solution # 3
sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)
fr = float(sr)
if fh > 40:
    #print("Overtime")
    reg = (fh * fr) # regular pay
    otp = (fh-40) * (fr * 0.5) # overtime pay
    #print(reg, otp)
    xp = reg + otp
else:
    #print("Regular")
    xp = fh * fr # regular pay
print("Pay:", xp)



# solution # 4

hrs = float(input("Enter hours:\n"))
rate = float(input("Enter rate:\n"))
if hrs > 40:
    print("Overtime")
    pay = (hrs-40)*rate*1.5 + 40*rate
else:
    print("Regular")
    pay = hrs * rate
print("Pay: ", pay)





