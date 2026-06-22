'''
Tell me the algorithm only.

Problem:

Ask the user for their age.

If the age is 18 or more, print:

You can vote

Now write the Python code.

Requirements:

Use int(input())
Use if
Print You can vote when age is 18 or more

'''

"""
Algorithm - 
Ask the user for age and store it in age.
Check if age is greater than or equal to 18.
If the condition is True, print "You can vote".

"""

age = int(input("What is your age: "))

if age >= 18:
    print("You can vote")

else:
    print("You can not vote")
          