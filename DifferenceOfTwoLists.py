a=[]
x=int(input("Enter Elements for List 1 "))

for i in range(0,x):
    y=int(input("Enter Values "))
    a.append(y)
print("List 1 ",a)



b=[]
c=int(input("Enter Elements for List 2 "))

for j in range(0,c):
    d=int(input("Enter Values "))
    b.append(d)

print("List 2 ",b)



e=set(a)-set(b)

f=list(e)

print("Difference in Two Lists ")

print(f)