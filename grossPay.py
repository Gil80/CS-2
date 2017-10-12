# Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input('Please enter amount of hours: ')
rate = input('Please enter rate per hour: ')
grossPay = float(hours) * float(rate)
print('The Gross Pay Amount is:',"$"+str(grossPay))