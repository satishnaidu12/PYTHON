#!/usr/bin/python3.10
import os
path=("/home/satish/test")
print(list(os.walk(path)))
print("--------------------------")
for each in os.walk(path):
    print(each)

