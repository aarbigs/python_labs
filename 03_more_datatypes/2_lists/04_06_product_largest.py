'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
number_list = []

for i in range(10):
    user_input = int(input("Please enter a number: "))
    number_list.append(user_input)

# id1 = int(input("Please enter a number: "))
# id2 = int(input("Please enter a number: "))
# id3 = int(input("Please enter a number: "))
# id4 = int(input("Please enter a number: "))
# id5 = int(input("Please enter a number: "))
# id6 = int(input("Please enter a number: "))
# id7 = int(input("Please enter a number: "))
# id8 = int(input("Please enter a number: "))
# id9 = int(input("Please enter a number: "))
# id10 = int(input("Please enter a number: "))
# empty_list.append(id1)
# empty_list.append(id2)
# empty_list.append(id3)
# empty_list.append(id4)
# empty_list.append(id5)
# empty_list.append(id6)
# empty_list.append(id7)
# empty_list.append(id8)
# empty_list.append(id9)
# empty_list.append(id10)

print(number_list)

sum_product = 1
for number in number_list:
    sum_product *= number

print(sum_product)

