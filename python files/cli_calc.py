x = int(input('Enter any number: '))
sign = input('Enter the arithmetic sign like + - * or /: ')
y = int(input('Enter another number: '))

if(sign == '+'):
    print(x+y)
elif(sign == '-'):
    print(x-y)
elif(sign == '*'):
    print(x*y)
else:
    print(x/y)