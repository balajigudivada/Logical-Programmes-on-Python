def perfect(num):
    sum=0
    for i in range(1,num):
        if (num%i==0):
            sum=sum+i
    if (sum==num):
        print('true')
    else:
        print('false')
perfect(6)