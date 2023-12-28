# Exercise 5: Program prompts user for a Celsius temperature, 
# convert the temperature to Fahrenheit, 
# and print out the converted temperature

Celsius = input("Enter temperature in Degree Celsius: ")
Celsius = int(Celsius)
Fahrenheit = (Celsius * (9/5)) + 32 
print(Fahrenheit, "Fahrenheit") 