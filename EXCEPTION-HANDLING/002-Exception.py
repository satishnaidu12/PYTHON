#!/usr/bin/python3.10
print("Welcome to excption concept")
print("Now it is fine")

try:
    #fo=open("/home/satish/test/sat.txt")
    fo=open("/home/satish/test/test.txt")
    print(fo.read())
    fo.close()
except:
    print("RUN TIME ERROR")
