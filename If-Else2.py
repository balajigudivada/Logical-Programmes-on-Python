'''Indus Bank accepts both short- and long-term deposits from its clients and offers an interest according to the scheme chosen.
If the amount is left in the bank as a fixed deposit for a period of 7 years, the interest rate given by the bank is 7.5% per annum, and for any other scheme that is lesser than 7 years, the interest rate is 4.5% per annum. Mr.Ravi wants to deposit Rs.50,000 in either short term or long term scheme based on the returns.
According to Mr.Ravi’s choice of the scheme, display the following details
• Interest amount he will get per annum.
• Interest amount he will for the entire term.
• Total Principal Amount + Interest for the entire term

Input:
Enter the Fixed Deposit Scheme [Long/Short]: Long
Expected Output:
Rs.50000 invested in long term scheme, Interest amount per annum is Rs.3750.0
Rs.26250.0 is the interest that Mr.Ravi will earn after 7 years

Input:
Enter the Fixed Deposit Scheme [Long/Short]: Short Enter the Term: 6
Expected Output:
Rs.50000 invested in short term scheme, Interest amount per annum is Rs.2250.0
Rs.13500.0 is the interest that Mr.Ravi will earn after 6 years'''

a=input('Enter the long/short term')
amt=int(input('Enter amount'))
if a=='long':
    print('Intrest per anum is',amt*(7.5/100),sep=' ')
    c=amt*(7*(7.5/100))
    print('Total intrest at the end of tenure',c,sep=' ')
    print('Total principle =',amt+c,sep=' ')
else:
    b=int(input('Enter tenure'))
    print('Intrest per anum is',amt*(4.5/100))
    x=amt*(b*(4.5/100))
    print('Total intrest at the end of tenure',x,sep=' ')
    print('Total principle=',amt+x,sep=' ')