#!/usr/bin/python3.10
import os
req_path=input("Enter your directory path: ")
#req_ex=input("Enter the required files extention .py/ .sh/ .log/ .txt: ")

if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. Please pass only directory path")
else:
    all_f_ds=os.listdir(req_path)
    if len(all_f_ds)==0:
        print(f"the given path is {req_path} an empty path")
    else:
        req_ex=input("Enter the required files extention .py/ .sh/ .log/ .txt: ")
        req_files=[]
        for each_f in all_f_ds:
            if each_f.endswith(req_ex):
                req_files.append(each_f)
        if len(req_files)==0:
            print(f"There are no {req_ex} files in the location of {req_path}")
        else:
            print(f"The required files are: {req_files}")
