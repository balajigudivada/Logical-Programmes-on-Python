'''Mr.Ben has started a new Food delivery company called “OnWheels”.
He has employed both Male and Female staffs for the position as Drivers. In that some are married while others are not. He has decided that the Drivers who are married should be provided with some extra benefits, So he decided to take insurance policies for those who are married, male and above 30yrs and also those who are married, female and above 25yrs.
Now help Mr.Ben to decide whether an employee is eligible for insurance or not.

Input:
Enter Name: Srikanth Enter Age: 32
Enter Gender: Male
Are you Married? [yes/no]: yes
Output:
Srikanth is eligible for Insurance

Input:
Enter Name: Srikanth Enter Age: 25
Enter Gender: Male
 
Are you Married? [yes/no]: yes
Output:
Srikanth is not eligible for Insurance

Input:
Enter Name: Srikanth Enter Age: 35
Enter Gender: Male
Are you Married? [yes/no]: no
Output:
Srikanth is not eligible for Insurance

Input:
Enter Name: Priya Enter Age: 26
Enter Gender: Female
Are you Married? [yes/no]: yes
Output:
Priya is eligible for Insurance

Input:
Enter Name: Priya Enter Age: 20
Enter Gender: Female
Are you Married? [yes/no]: yes
Output:
Priya is not eligible for Insurance

Input:
Enter Name: Priya Enter Age: 28
Enter Gender: Female
Are you Married? [yes/no]: no
Output:
Priya is not eligible for Insurance'''

n=input('Enter name')
g=input('Enter Gender')
a=int(input('Enter Age'))
m=input('Married/Not Married [yes/no]:')
if g=='male':
        if a>=30 and m=='yes':
            print(n,'is eligible for insurence',sep=' ')
        else:
             print(n,'Not eligibile for insurence',sep=' ')  
            
elif g=='female':
    if a>=25 and m=='yes':
            print(n,'is eligibile for insurence',sep=' ')
    else:
            print(n,'Not eligibile for insurence',sep=' ')
        
    
    