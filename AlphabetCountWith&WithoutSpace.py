str=input("Enter string ")
print("withspaces: ",len(str))
count=0;
for ch in str:
    if ch!=' ':
        count=count+1
print("without spaces: ",count)