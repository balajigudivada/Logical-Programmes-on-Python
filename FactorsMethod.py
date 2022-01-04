def factors(num):
    for i in range(1,num):
        if (num%i==0):
            print(i,end=' ')
factors(6)