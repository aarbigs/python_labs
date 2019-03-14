'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

string_1 = input("Please enter string 1: ")
string_2 = input("Please enter string 2: ")
string_3 = input("Please enter string 3: ")


st1 = (string_1.count(""))
st2 = (string_2.count(""))
st3 = (string_3.count(""))

if st1 > st2 and st1 > st3:
    print(st1)
elif st2 > st1 and st2 > st3:
    print(st2)
else:
    print(st3)