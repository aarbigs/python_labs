'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:
'''

user_input = "hello"
new_dict = {}
#result = {"h": 1, "e": 1, "l": 2, "o": 1}

for i in user_input:
    new_dict[i] = user_input.count(i)

print(new_dict)