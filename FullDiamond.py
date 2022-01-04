for i in range(0,5):
    for j in range(i,4):
        print(' ',end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
        print(' ',end=' ')
    print()
for i in range(3,-1,-1):
    for j in range(i,4):
        print(' ',end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
        print(' ',end=' ')
    print()