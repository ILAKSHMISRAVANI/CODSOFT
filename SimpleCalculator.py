# Simple Calculator for basic arithmetic operations
print('Simple Calculator')
print('--------------------------------------------')
n,m=int(input('enter first number:')),int(input('enter second number:' ))
st='+-*/'
print('Different operations\n 1.Addition +\n 2.Subtraction -\n 3.Multiplication *\n 4.Division /')
mode=input('enter arithmetic operator:')
print('Result is:')
if mode in st:
    if mode =='+':
        print(n+m)
    elif mode =='-':
        print(n-m)
    elif mode =='*':
        print(n*m)
    else:
        print(n/m)
    print('----------------------------------------')
else:
    print('enter a valid arithmetic operator ')
    print('---------------------------------------')
