'''
Code a game of rock paper scissors.

'''
from random import randint


player = int(input("Please enter a number: 0 = scissor, 1 = rock, 2 = paper: "))
# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        print("scissor")
        return "scissor"
    elif hand == 1:
        print("rock")
        return "rock"
    else:
        print("paper")
        return "paper"
    # for example if the variable hand is 0, it should return the string "scissor"
    pass

get_hand(player)

computer = randint(0, 2)
print(str(computer))


# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if computer > player:
        print("You lost :(")
    elif computer < player:
        print("You won!")
    else:
        print("You tied!")
    pass


determine_winner(computer, player)

# take in a number 0-2 from the user that represents their hand

# generate a random number 0-2 to use for the computer's hand





# call the function get_hand to get the string representation of the user's hand

# call the function get_hand to get the string representation of the computer's hand

# call the function determine_winner to figure out the winner

# print out the player hand and computer hand

# print out the winner