'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:
'''

input_string = "hello world"
str_split = input_string.split(" ")

new_str = []
for i in str_split:
    new_str.append(tuple(i))
print(new_str)
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

