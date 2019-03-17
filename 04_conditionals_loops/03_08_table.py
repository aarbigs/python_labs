'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''

for i in range(0, 41, 10):
    print()
    for n in range(0, 10):
        print(i + n, (i+1)+n, (i+2)+n, (i+3)+n, (i+4)+n, (i+5)+n, (i+6)+n, (i+7)+n, (i+8)+n)
    print(" ")

# I'm not sure how to get this to work?
    