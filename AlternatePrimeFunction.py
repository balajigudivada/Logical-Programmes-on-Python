def alternatePrime(num1,num2):
    x=0
    for i in range(num1,num2):
        count=0
        for j in range(1,i):
            if (i%j==0):
                count+=1
        if count<=1:
            x+=1
            if x%2==0:
                print(i)
alternatePrime(1,100)