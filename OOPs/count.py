#!/usr/bin/python3.10
class emp:
    count=0
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.increase_count_for_emp()
    def increase_count_for_emp(self):
        emp.count=emp.count+1
    def display_details(self):
        print(f"The name is: {self.name}\n the age is: {self.age}\n The salary is: {self.salary}")
        return None

emp1=emp()
emp2=emp()

emp1.get_name_age_salary("abc",34,"999999")
#emp1.increase_count_for_emp() Added in line 7
emp2.get_name_age_salary("abcd",35,"9999999")
#emp2.increase_count_for_emp() Added in line 7

print(emp.count)
