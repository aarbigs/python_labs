'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''

import os
cwd = os.getcwd()
print(cwd)
print(os.path.abspath('words.txt'))
# count = 0
# for(dirname, dirs, files) in os.walk('.'):
#     for filename in files:
#         if filename.endswith('.jpg'):
#             count += 1
#
# print(files, count)

'''I'm having trouble changing the directory to begin this problem?'''