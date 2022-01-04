a=[]
x=int(input("Enter Elements "))

for i in range (0,x):
    y=int(input())
    a.append(y)

print("List Elements ")

print(a)

print("Enter Element check it is Present or not")

z=int(input())

for i in a:
   if i==z:
       print("Element Exist")