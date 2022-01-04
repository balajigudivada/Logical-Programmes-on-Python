l=[]
n=int(input('Enter n value '))
for i in range(0,n):
    n=int(input())
    l.append(n)
x= len(l)
for i in range(0,x):
    count=1
    for j in range (i+1,x):
        if l[i]==l[j]:
            count+=1
            l[j]=None
    if count>1 and l[i]!=None:
        print(l[i],end=' ')