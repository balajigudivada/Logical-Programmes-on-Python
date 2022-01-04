str=input("Enter string ")
vcount=0;
ccount=0;
for ch in str:
    if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            vcount=vcount+1;
        else:
            ccount=ccount+1
print("Number of vowels: ",vcount)
print("Number of Consonents: ",ccount)