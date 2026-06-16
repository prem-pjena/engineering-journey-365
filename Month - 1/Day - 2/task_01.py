'''
Problem

Create a program that asks the user for their:

Name
Age

And then prints:

Hello Prem
You are 24 years old
'''

name = input("What is your name: ")
age = int(input("What is your age: "))

print("Hello", name)
print(f"Your are {age} years old")