str=input("Enter string ")
words=str.split(" ")
count=0
for word in words:
    for ch in word:
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            count=count+1
    print(word," : ",count)
    count=0