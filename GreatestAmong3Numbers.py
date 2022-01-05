a=int(input('Enter number 1 '))
b=int(input('Enter number 2 '))
c=int(input('Enter number 3 '))
if a>b and a>c:
    print(a,'Is greater')
elif b>a and b>c:
    print(b,'Is greater')
else:
    print(c,'Is greater')