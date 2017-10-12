# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

cTemp = input('Enter temperature value in Celsius: ')
fTemp = (((float(cTemp) * 9) / 5) + 32) # formula to convert from C to F temperature values
print('The Farenheit temperature value is:',str(round(fTemp, 2))+'F')