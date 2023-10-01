#!/usr/bin/python3.10
class Emp(object):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.display()
        return None
    
    def display(self):
        print(f"The name is: {self.name}\n the salary is: {self.salary}")
        return None

emp1=Emp("abc",99999999)
#emp1.display() #added in line 6

emp2=Emp("abcd",999999999)
#emp2.display() #added in line 6
