class Itemtype:
    def __init__(self,n,d,c):
        self.name=n
        self.deposit=d
        self.costperday=c
    def display(self):
        print(self.name,self.deposit,self.costperday)
item1=Itemtype("pen",12,300)
item1.display()
item2=Itemtype("chair",24,450)
item2.display()