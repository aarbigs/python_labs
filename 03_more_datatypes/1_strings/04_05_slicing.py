'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

usr_name = input("Please enter a name: ")
piglatin = usr_name[1:] + usr_name[0] + "ay"
print(piglatin)