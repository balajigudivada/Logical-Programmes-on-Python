class Itemtype:
    def __init__(self):
        self.name=input("enter name")
        self.deposit=int(input("Enter amount"))
        self.costperday=int(input("enter costperday"))
    def display(self):
        print(self.name,self.deposit,self.costperday)
item1=Itemtype()
item1.display()
item2=Itemtype()
item2.display()
