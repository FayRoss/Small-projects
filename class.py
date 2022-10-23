
# --init-- (initializes the attributes and its automatically executed with every new class instance and it has a reserved name)
#The self paremeter always represents the current instance of the class

class Person:
    def __init__(self,n,g,a):
        self.name=n
        self.gender=g
        self.age=a

def talk(self):
    print("Hi I am",self.name)

def vote(self):
    if self.age<18:
        print("I am not eligable to vote")
    else:
        print("I am eligable to vote")

per1=Person("Fay","Female", 16)             
per2=Person("Mahir","Male",24)

print(per1.name)
print(per2.name)

print("Hi, I am", per1.name)

per1.talk()
per1.vote()





