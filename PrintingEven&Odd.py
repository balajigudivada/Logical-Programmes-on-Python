li=[]
x=int(input("Enter Elements "))

for i in range(0,x):
   y=int(input("Enter Values "))
   li.append(y)

print(li)

print("Even Numbers ")

for i in li:
   if i%2==0:
       print(i,end=' ')

print('\n')

print("Odd Numbers ")

for j in li:
   if j%2!=0:
       print(j,end=' ') 