#!/usr/bin/python3.10
class Emp:
    def __init__(self):
        print("This is a init method")
        return None
    def display(self):
        print("This is a display method")
        return None

emp1=Emp()
emp2=Emp()

emp1.display()
emp2.display()

print(f"=================Emp1 starting =================")

class Emp1:
    count=0
    def __init__(self):
        Emp1.count=Emp1.count+1
        print("This is a init method")
        return None
    def display(self):
        print("This is a display method")
        return None

emp1=Emp1()
print (f"The number of objects created from Emp1 class are: ",Emp1.count)
