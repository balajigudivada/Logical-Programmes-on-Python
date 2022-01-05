class Laptop:
    def read(self):
        self.brand=input("enter brand name")
        self.color=input("Enter color")
        self.modelno=int(input("Enter Model no"))
    def display(self):
#self parameter refernce varaible of a current
        print(self.brand,self.color,self.modelno)
hp=Laptop()
hp.read()
hp.display()
dell=Laptop()
dell.read()
dell.display()
