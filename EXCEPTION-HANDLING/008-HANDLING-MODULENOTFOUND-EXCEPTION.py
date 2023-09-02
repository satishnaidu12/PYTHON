#!/usr/bin/python3.10
try:
    #print(4+"hi")
    #open('abcd.txt')
    #print(5/0)
    import fabric
except FileNotFoundError:
    print("File is not available")
except ZeroDivisionError:
    print("Zero Division is not possible")
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Adding number and string is not possible")
except ModuleNotFoundError:
    print("Please install fabric module")
except Exception as e:
    print(e)
