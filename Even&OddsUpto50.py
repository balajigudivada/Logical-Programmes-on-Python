n=int(input('enter n value'))
i=1
print('even numbers are')
while(i<=50):
    if i%2==0:
        print(i,end=' ')
    i=i+1
print('')
print('odd numbers are')
for i in range(1,n,2):
    print(i,end=' ')
