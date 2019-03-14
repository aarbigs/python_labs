'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

string_input = input("Please enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
count = 0
for letter in string_input:
    if letter in vowels:
        count += 1
print(count)