class Student:
    #non-parameterized
    def __init__(self):
        self.id=int(input("id"))
        self.name=input("name")
    def display(self):
        print(self.id,self.name)
st1=Student()
st1.display()
st2=Student()
st2.display()