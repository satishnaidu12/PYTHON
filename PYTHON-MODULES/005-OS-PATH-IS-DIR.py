#!/usr/bin/python3.10
import os
path="/home/satish"

if os.path.isdir(path):
    print(f"{path} is a DIR")
else:
    print(f"{path} is NOT a DIR")
