'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

for i in range(1,100):
    if i % 2 == 0:
        continue
    else:
        print(i)