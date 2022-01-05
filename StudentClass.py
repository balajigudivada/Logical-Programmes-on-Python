'''Student
id,name,branch
display()
insert()'''
class Student:
    def read(self):
        self.name=input("enter name")
        self.id=int(input("enter id"))
        self.branch=input("enter branch")
    def display(self):
        print(self.name,self.id,self.branch)
st1=Student()
st1.read()
print("Student 1 details")
st1.display()
st2=Student()
st2.read()
print("Student 2 details")
st2.display()