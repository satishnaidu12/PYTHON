#!/usr/bin/python3.10
#method 1
#class Emp
#method 2

class Emp(object):
    def name_salary(self,name,salary):
        self.name=name
        self.salary=salary
        return None
    def display(self):
        print(f"The name is: {self.name}\n The Salary is: {self.salary}")
        return None

emp1=Emp()
emp2=Emp()
emp1.name_salary("abc",9999999)
emp2.name_salary("abcd",99999999)


emp1.display()
emp2.display()

