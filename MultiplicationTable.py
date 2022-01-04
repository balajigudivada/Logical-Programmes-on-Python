n=int(input('Enter number '))
a=1
while(a!=0):
    i=1
    while(i<=10):
        print(n,'*',i,'=',n*i)
        i+=1
    a=int(input('Do you want to continue printing the table, press 1 or 0 to Exit:'))
    n=n+1   
    
