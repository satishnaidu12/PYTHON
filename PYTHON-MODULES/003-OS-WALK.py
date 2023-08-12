#!/usr/bin/python3.10
import os
path=("/home/satish/test")
#for r,d,f in os.walk(path):
#    print(r,d)
#for a,b,c in os.walk(path,topdown=False):
for r,d,f in os.walk(path):
    if len(f) !=0:
        print(r,d,f)

