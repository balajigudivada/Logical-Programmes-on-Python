n=int(input('Enter n value'))
i=1
for i in range(1,n):
    if i%2!=0:
        if i%3!=0:
            print(i,end=' ')