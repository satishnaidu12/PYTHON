#!/usr/bin/python3.10
import os
req_path=input("Enter your directory path: ")
req_ex=input("Enter the required files extention .py/ .sh/ .log/ .txt: ")

if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. Please pass only directory path")
else:
    print("Implement your actual logic")
