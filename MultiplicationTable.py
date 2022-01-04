n=int(input('Enter n value '))
i=1
while (i<=10):
    v=i*n
    print(n,'*',i,'=',v,sep=' ')
    i=i+1
a=int(input('Do you want to continue printing the table, press 1 or 0 to Exit:'))
while(a!=0):
    n=n+1
    for i in range(1,11):
        b=n*i
        print(n,'*',i,'=',b,sep=' ')
    a=int(input('Do you want to continue printing the table, press 1 or 0 to Exit:'))
        
    