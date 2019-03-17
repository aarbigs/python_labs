'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

upper = int(input("please enter the upper bound: "))
lower = int(input("please enter the lower bound: "))
new_sum = 0
for i in range(lower, upper+1):
    new_sum += lower
    lower += 1

print(new_sum)
