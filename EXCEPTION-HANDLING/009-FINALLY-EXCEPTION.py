#!/usr/bin/python3.10
try:
    print("This is simple exception")
    print(a)
except NameError:
    print("Variable is not define")
except Exception as e:
    print(e)
finally:
    print("This will excute after trying with try and except blocks")
