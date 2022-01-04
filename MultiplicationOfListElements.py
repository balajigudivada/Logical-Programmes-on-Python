a=[]
x=int(input("Enter Elements "))

for i in range(0,x):
    y=int(input())
    a.append(y)

print("List of Elements ",a)


sum=1
for i in a:
    sum=i*sum
print("After Multiplication list list elements result is ")
print(sum)