n=int(input('Enter number '))
temp=n
count=len(str(n))
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem**count
    n=n//10
if temp==sum:
    print('Amstrong')
else:
    print('Not Amstrong')