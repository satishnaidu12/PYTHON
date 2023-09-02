#!/usr/bin/python3.10
def myfunction1():
    x=60 #This is local variable.
    print("welcome to python function")
    print("x value from fun1: ", x)
    myfunction2()
    return None
def myfunction2():
    print("Thank you")
    print("x value from fun2: ", x)
    return None
x=10 #This global variable.
myfunction1()
