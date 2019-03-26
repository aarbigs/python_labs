'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
words = []
counter = 0
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        words.append(word)
        counter += 1
        if counter == 20:
            break

size = len(words)
hiindex = size - 1
its = int(len(words)/2)              # Number of iterations required
for i in range(0, its):    # i is the low index pointer
    temp = words[hiindex]     # Perform a classic swap
    words[hiindex] = words[i]
    words[i] = temp
    hiindex -= 1            # Decrement the high index pointer
print("Done!")
#reverse_words = words.reverse()

#print(words[::-1])
#print(reverse_words)
print(words)