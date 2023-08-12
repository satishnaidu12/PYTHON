#!/usr/bin/python3.10
import os
path="/home/satish/file_link.txt"

if os.path.islink(path):
    print(f"{path} is a link file")
else:
    print(f"{path} is NOT a link file")
