l=[]
#for reading user input into list
n=int(input('Enter n value'))
for i in range(0,n):
    n=int(input())
    l.append(n)
#for removing duplicate values
x= len(l)
i=0
while (i<x):
    j=i+1
    while(j<x):
        if l[i]==l[j]:
            l.pop(j)
            x=len(l)
            j=j-1
        j=j+1
    i=i+1
print(l)