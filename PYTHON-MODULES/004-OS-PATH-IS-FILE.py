#!/usr/bin/python3.10
import os
path="/home/satish/file.txt"

if os.path.isfile(path):
    print(f"{path} is a file")
else:
    print(f"{path} is NOT a file")
