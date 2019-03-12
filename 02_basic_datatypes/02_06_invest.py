'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

invest = int(input("enter investment amount: "))
interest = int(input("enter interest rate: "))
num_years = int(input("enter number of years: "))
fv = invest * ((1+(interest/100))**num_years)
print(fv)