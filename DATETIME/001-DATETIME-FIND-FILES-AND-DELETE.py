#!/usr/bin/python3.10
import os
import sys
req_path=input("Enter your path: ")
age=30
if not os.path.exists(req_path):
    print("Please provide valid path ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path")
    sys.exist(2)
print(os.listdir(req_path))
