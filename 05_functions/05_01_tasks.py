'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

num_input = int(input("Please enter a number betwee 1 and 1,000,000,000: "))

def div_by_7_and_4(input):
    if input % 7 == 0 and input % 4 == 0:
        print("Divisible 7 and 4!")
        return True

def div_by_7_or_4(input):
    if input % 7 == 0 or input % 4 == 0:
        print("Divisible by 7 or 4!")
        return True


div_by_7_and_4(num_input)
div_by_7_or_4(num_input)