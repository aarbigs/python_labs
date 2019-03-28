'''
Write a script that demonstrates a try/except/else.

'''

try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    print(num1/num2)
except Exception as exc:
    print("exception error")
else:
    print("Congratulations no exceptions")