#!/usr/bin/python3.10
try:
    #print(4+"hi")
    #open('abcd.txt')
    print(5/0)
except FileNotFoundError:
    print("File is not available")
except ZeroDivisionError:
    print("Zero Division is not possible")
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Adding number and string is not possible")
except Exception as e:
    print(e)
