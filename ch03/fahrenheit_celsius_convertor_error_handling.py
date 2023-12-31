# try except error handling:
# Program that converts temperature Fahrenheit to celsius 

temp = 32 #"5 degrees" # string
cel = 0
try:
    fahr = float(temp) # cannot float a str
    cel = (fahr-32.0) * 5.0/9.0
except:
    print('Error, enter a numerical number')
    quit()
print(cel)



