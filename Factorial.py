num=int(input('Enter number '))
fact=1
if(num<0):
    print('sorry can not find')
elif (num==0):
    print('sorry can not find')
else:
    for i in range (1,1+num):
        fact=fact*i
print(fact)