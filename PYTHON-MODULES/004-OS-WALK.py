#!/usr/bin/python3.10
import os
path=("/home/satish/test")
for r,d,f in os.walk(path):
    if len(f) !=0:
        print(r,d)
        for each_file in f:
            print(os.path.join(f,each_file))

