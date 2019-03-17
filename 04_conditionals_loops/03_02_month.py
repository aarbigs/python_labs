'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

user_input = int(input("Please enter a month number: "))

if user_input == 1:
    print("January")
elif user_input == 2:
    print("February")
elif user_input == 3:
    print("March")
#etc..
else:
    print("Other")