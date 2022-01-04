def febnocci(num1,num2):
    num1=0
    num2=1
    n=int(input('Enter the range '))
    for i in range(1,n):
        num3=num1+num2
        print(num3,end=' ')
        num1=num2
        num2=num3
febnocci(1,10)