#!/usr/bin/python3.10
try:
    #a=10
    print(a)
except NameError:
    print("variable is not defined")
except Exception as e:
    print("Exception occurred: ", e)
else:
    print("This will execute if NO Exception in the try block")
finally:
    print("This will always excute")
