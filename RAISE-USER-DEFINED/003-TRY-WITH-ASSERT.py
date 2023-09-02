#!/usr/bin/python3.10
age=20
try:
    #assert age>30
    assert age<30
    print("Valid age")
except AssertionError:
    print("Raised with assert because age is lessthan 30")
except:
    print("Exception occured")
