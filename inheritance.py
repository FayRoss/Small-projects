#Types of inheritance 1. Single(A-B, B inherits from A), Multilevel(A-B-C, C inherits from A), Multiple(A-B-C, C inherits from both A&B)

from cmd import IDENTCHARS
from unicodedata import name


class A:
    def feature1(self):
         print("feature1 is working")

class B:
    def feature2(self):
        print("feature2 is working")


class C(A,B):
    def feature3(self):
        print("feature3 is working")

a1=A()            
a1.feature1()
a2=B()
a2.feature2()

b1=B()
b1.feature2()

c1=C()
c1.feature1()


class Parent:
    def function1(self):
        print("This is a parent class")

class Child(Parent):
    def function2(self):
        print("This is a child class")

obj=Child()
obj.function1()
obj.function2()
 
 # the --init-- fxn gets automatically called every time an object is created for a class
class Parent:
    def __init__(self, fname,fage):
        self.name=fname
        self.age=fage
    
    def view(self):
        print(self.name,self.age)

class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname= "Ross"
    
    def view(self):
        print(self.age, self.lastname, self.name)

obj=Child(23,"Fay")
obj.view()









class Employee:
    def __init__(self,fname,fID,fdeper):
        self.name=fname
        self.ID=fID
        self.deperment=fdeper
    
    def view(self,fname,fID,fdeper):
        print(self.name,self.ID,self.deper)
    
class Depertment(Employee):
    def __init__(self,fname,fID,fdeper):
        Employee.__init__(self,fname,fID,fdeper)
        self.name=fname
        self.ID=fID
        self.derpertment=fdeper
    
    def view(self):
        print(self.name,self.ID,self.deperment)  

emp1=Depertment("Mahir",24, "Accounts")
emp1.view()


    
        
        