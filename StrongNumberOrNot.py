num=int(input('Enter Number'))
sum=0
temp=num
while (num!=0):
    rem=num%10
    fact=1
    while(rem!=0):
        fact=fact*rem
        rem-=1
    sum=sum+fact
    num=num//10
if temp==sum:
    print('Given number is a strong number')
else:
    print('Not a strong  number')