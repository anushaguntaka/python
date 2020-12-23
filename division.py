# 6)Write a Python program to Accept two digits and print their Quotient and Remainder and display the error message if divisor is Zero then display error message?

num1 = input("enter number to be divided:")
num2 = input("enter number to be divisable:")
if int(num2) == 0:
    print("any number cannot be divided with zero")
else:
    remainder = int(num1) % int(num2)
    quotient = int(num1) / int(num2)
    print("quotient", quotient)
    print("Remainder", remainder)

