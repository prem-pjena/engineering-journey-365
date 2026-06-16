'''
Problem

Ask the user for two numbers.

If the first number is larger:

First Number is Larger

If the second number is larger:

Second Number is Larger

If both are equal:

Both Numbers are Equal
'''

'''
Algorithm - 
Ask the user for the first number and store it.
Ask the user for the second number and store it.
Check if the first number is greater than the second number.
If True, print First Number is Larger.
Otherwise, check if the second number is greater than the first number.
If True, print Second Number is Larger.
Otherwise, print Both Numbers are Equal.
'''

num1 = int(input("gie me num1: "))

num2 = int(input("gie me num2: "))

if num1 > num2:
    print("First Number is Larger")

elif num2 > num1:
    print("Second Number is Larger")

else:
    print("Both Numbers are equal")
