'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

user_input = int(input("Please enter a number between 1 and 1 million: "))

if user_input % 3 == 0:
    print("Divisible by Three")
else:
    print("not divisible by three")