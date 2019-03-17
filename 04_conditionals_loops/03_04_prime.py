'''
Print out every prime number between 1 and 100.

'''

for p in range(1, 100):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print(p)
print('Done')