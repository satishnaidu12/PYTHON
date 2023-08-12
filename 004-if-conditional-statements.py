#!/usr/bin/python3.10
usr_str=input("Enter your string: ")
usr_cnf=input("Do you want to convert your given string into title fmt: ?")
if usr_cnf=="yes":
    print(usr_str.title())
else:
    print(usr_str)
