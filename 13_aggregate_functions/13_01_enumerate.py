'''
Demonstrate the use of the .enumerate() function.
'''

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 0):
    print(c, value)

for c, value in enumerate(my_list, 10):
    print(c, value)

new_list = list(enumerate(my_list))
print(new_list)

