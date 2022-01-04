str=input("Enter string ")
acount=0
ecount=0
Icount=0
Ocount=0
Ucount=0
Consonants=0
for ch in str:
    if ch=='a' or ch=='A':
        acount=acount+1
    elif ch=='e' or ch=='E':
        ecount=ecount+1
    elif ch=='i' or ch=='I':
        Icount=Icount+1
    elif ch=='o'or ch=='O':
        Ocount=Ocount+1
    elif  ch=='u' or ch=='U':
        Ucount=Ucount+1
    elif ch>='a' and ch <='z' or ch>='A' and ch<='Z':
        Consonants=Consonants+1
print("a=",acount)
print("e=",ecount)
print("i=",Icount)
print("o=",Ocount)
print("u=",Ucount)
print("Consonants=",Consonants)