#!/usr/bin/python3.10
class emp:
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display_details(self):
        print(f"The name is: {self.name}\n the age is: {self.age}\n The salary is: {self.salary}")
        return None

emp1=emp()
emp2=emp()

emp1.get_name_age_salary("abc",34,"999999")
emp2.get_name_age_salary("abcd",35,"9999999")

print(dir(emp1))

print(f"=============111111111111111============")

print(emp1.age)

print(f"=============222222222222222222=========")

emp1.display_details()
