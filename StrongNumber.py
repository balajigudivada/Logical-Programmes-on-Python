num1=int(input('Enter Number1 '))
num2=int(input('Enter Number2 '))
for i in range(num1,num2):
    sum=0
    temp=i
    while(i!=0):
        rem=i%10
        fact=1
        while(rem!=0):
            fact=fact*rem
            rem-=1
        sum=sum+fact
        i=i//10
    if sum==temp:
        print(temp)