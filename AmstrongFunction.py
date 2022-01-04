def amstrong(n):
    temp=n
    sum=0
    s=len(str(n))
    while (n!=0):
        rem=n%10
        sum=sum+(rem**s)
        n=n//10
    if sum==temp:
        print('Given number is a amstrong')
    else:
        print('Given number is not amstrong')
amstrong(153)