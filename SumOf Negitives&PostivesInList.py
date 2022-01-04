list=[10,50,-30,15,-45,-96,5,78,-99,253]
sum=0
for i in list:
    if i<0:
        sum=sum+i
print('Sum of Negative Numbers =',sum,sep=' ')
sum=0
for i in list:
    if i>0:
        sum=sum+i
print('Sum of Positive Numbers =',sum,sep=' ')
