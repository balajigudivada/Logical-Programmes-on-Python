'''Mr.Kumar went to purchase stationary items for his office. He asked the shopkeeper for a discount. The shopkeeper said that if he purchases more than 200 quantity of the item, then a discount of 20% can be applied on the total bill amount, excluding the GST.
Get the Quantity and price per item as an input and calculate and tell whether Mr.Kumar is eligible for the discount and what would be the net amount he has to pay after the discount.
Take the GST at 18%.
Net Amount = Total bill amount after discount + GST

Input-
Enter the required Quantity: 100
 
price per unit is:Rs.5
Output:
Quantity Ordered 100 Price per item is Rs.5 Total Amount = Rs.500 GST - Rs.90.0
Net Amount Payable is Rs.590.0

Input-
Enter the required Quantity: 350 price per unit is :Rs.20
Output:
Quantity Ordered 350 Price per item is Rs.20 Total Amount = Rs.7000
Discount Earned = Rs.1400.0 Amount after Discount - Rs.5600.0 GST - Rs.1008.0
Net Amount Payable is Rs.6608.0'''

q=int(input('Enter the quantity'))
p=int(input('Enter the price'))
if q>=200:
    x=q*p
    print('Total amount=',x,sep=' ')
    d=x*(20/100)
    print('Discount earned=',d,sep=' ')
    y=x-d
    print('After Discount=',y,sep=' ')
    gst=x*(18/100)
    gst+=y
    print('Net amount payble',gst,sep=' ')
else:
    x=q*p
    print('Total amount=',x,sep=' ')
    gst=x*(18/100)
    print('GST =',gst,sep=' ')
    gst+=x
    print('Net amount payble',gst,sep=' ')
    

