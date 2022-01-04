for row in range(0,5):
    for col in range(0,5):
        if (row==0 and col%4==0) or (row==1 and col%2!=0) or (row==2 and col==2) or (row==3 and col%2!=0) or (row==4 and col%4==0):
            print('$',end='  ')
        else:
            print('*',end='  ')
    print(' ')