#!/usr/bin/python3.10
try:
    #print(4+"hi")
    open('abcd.txt')
except FileNotFoundError:
    print("File is not available")
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Adding number and string is not possible")
except Exception as e:
    print(e)
