#!/usr/bin/python3.10
import sys
#Try second
usr_str=sys.argv[1]
usr_action=sys.argv[2]
#TRY 1st
#usr_str=input("Enter your string: ")
#usr_action=input("Enter your action on your string (valid actions are: lower/upper/title): ")
if usr_action=="lower":
    print(usr_str.lower())
elif usr_action=="upper":
    print(usr_str.upper())
elif usr_action=="title":
    print(usr_str.title())
else:
    print("your option is invalid. Please select valid option from this list: lower/upper/title")
