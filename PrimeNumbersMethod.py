def prime(num):
    count=0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               count=count+1
    if(count==0):
        print('true')
    else:
        print('false')
prime(6)