'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

#usr_string = input("Please enter a string: ")
usr_string = "hi hi hi hi how are you you you"
str_list = usr_string.split()
counts = dict()
most_word = ""
words = sorted(set(str_list))
for word in str_list:
    if word in counts:
        counts[word] += 1
        most_word = word
    else:
        counts[word] = 1

print(most_word)

