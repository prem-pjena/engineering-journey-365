'''
Problem

Ask the user for a number.

If the number is greater than 0:

Positive

If the number is equal to 0:

Zero

Otherwise:

Negative

'''

'''
Algorithm - 
create a variabele num then collect input from user use typecasting for int and store it in the num.
then comare with zero
if greater than zero then print positive
if equal to zero then print zero
if not then print negative

'''


num = int(input("Write a number: "))

if num > 0:
    print("Positive")

elif num == 0:
    print("Zero")

else:
    print("Negative")
