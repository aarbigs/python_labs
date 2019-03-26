'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
long_words = []
counter = 0
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        counter += 1
        if len(word) >= len(long_words):
            long_words = word

short_words = []
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        if len(word) <= len(short_words):
            short_words = word

print(short_words)
print(counter)
print(long_words)