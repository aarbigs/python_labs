'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

gen_list = [i*2 for i in range(5)]
print(type(gen_list))
for i in gen_list:
    print(i)

gen = (i*2 for i in range(5))
print(type(gen))
for i in gen:
    print(i)