#!/usr/bin/python3.10
print("Welcome to exception concept")
print("Now it is fine")
'''
fo=open("/home/satish/test/filea.txt")
print(fo.read())
fo.close()
'''

try:
    fo=open("/home/satish/test/filea.txt")
    #fo=open("/home/satish/test/file.txt")
    print(fo.read())
    fo.close()
except Exception as e:
    print("This is because ",e)
