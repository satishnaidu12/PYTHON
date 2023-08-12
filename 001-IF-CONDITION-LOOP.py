#!/usr/bin/python3.10
import os
import sys
path=input("ENTER YOUR DIRECTORY PATH: ")
list_of_files_dir=os.listdir(path)
print("ALL files and dirs: ",list_of_files_dir)
for each_file_or_dir in list_of_files_dir:
    print(each_file_or_dir)
