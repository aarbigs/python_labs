'''

Write a script that removes all duplicates from a list.

'''

new_list = []
id1 = int(input("Please enter a number: "))
id2 = int(input("Please enter a number: "))
id3 = int(input("Please enter a number: "))
id4 = int(input("Please enter a number: "))
id5 = int(input("Please enter a number: "))
new_list.append(id1)
new_list.append(id2)
new_list.append(id3)
new_list.append(id4)
new_list.append(id5)


print(set(new_list))

