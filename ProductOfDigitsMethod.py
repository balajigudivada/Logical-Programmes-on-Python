def digitsproduct(num):
    l=len(str(num))
    res=1
    if num>10:
        for i in range(l):
            rem=num%10
            res=res*rem
            num=num//10
    else:
        print('enter a number greater than 10')
    print(res)
digitsproduct(555)