#!/usr/bin/python3.10
'''
def display(a,b):
    print(a)
    print(b)
    return None
display(4,5)
display(b=5,a=4)
display(a=4,b=5,c=6)
'''
#karg is variable.
def display(**karg):
    print(karg)
    return None
#OUTPUT will come dictionary format.
display(b=5,a=4)
display(a=4,b=5,c=6)
print("==============================")
print("We are assinging 56 to p variable")
def display1(p,**karg):
    print(p)
    print(karg)
    return None
display1(56,y="hi",z=6.7,user="root")
