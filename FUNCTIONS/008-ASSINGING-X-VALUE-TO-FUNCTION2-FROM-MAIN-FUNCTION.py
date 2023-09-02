#!/usr/bin/python3.10
def myfunction1():
    x=60 #This is local variable.
    print("welcome to python function")
    print("x value from fun1: ", x)
    return None
def myfunction2(y): #Parameter
    print("Thank you")
    print("x value assigned to y from main function to myfunction2")
    print("y value from fun2: ", y)
    return None
def main():
    #global x #NOT a good practice.
    x=10
    myfunction1()
    myfunction2(x) #Argument
    return None
main()
