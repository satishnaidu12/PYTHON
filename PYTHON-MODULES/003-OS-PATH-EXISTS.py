#!/usr/bin/python3.10
import os
path="/home/satish/file.txt"
print(os.path.basename(path))
print(os.path.dirname(path))

if os.path.exists(path):
    print("your file is available")
else:
    print(f'{path} is not present on this server')
