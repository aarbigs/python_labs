'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

'''new_list = []
id1 = int(input("Please enter a number: "))
id2 = int(input("Please enter a number: "))
id3 = int(input("Please enter a number: "))
id4 = int(input("Please enter a number: "))
id5 = int(input("Please enter a number: "))
id6 = int(input("Please enter a number: "))
id7 = int(input("Please enter a number: "))
id8 = int(input("Please enter a number: "))
id9 = int(input("Please enter a number: "))
id10 = int(input("Please enter a number: "))
new_list.append(id1)
new_list.append(id2)
new_list.append(id3)
new_list.append(id4)
new_list.append(id5)
new_list.append(id6)
new_list.append(id7)
new_list.append(id8)
new_list.append(id9)
new_list.append(id10)'''

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 1
while count < 10:
    print(mylist[count])
    count +=2

count = 8
while count > -1:
    print(mylist[count])
    count -=2