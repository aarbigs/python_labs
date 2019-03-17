'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

user_input = int(input("Please enter a number between 0 and 1 Million: "))
guess = 0
while guess != user_input:
    guess += 1
    if guess == user_input:
        print("Your number was "+str(guess))
        break