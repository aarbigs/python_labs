'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

string_input = input("Please enter a string: ")
letter_input = input("Please enter a letter in the string to find: ")

print(string_input.find(letter_input))