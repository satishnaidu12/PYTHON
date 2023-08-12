#!/usr/bin/python3.10
import os
import sys
path=("/home/satish/test")
list_of_files_dir=os.listdir(path)
print("ALL files and dirs: ",list_of_files_dir)
for each_file_or_dir in list_of_files_dir:
    f_d_p=os.path.join(path,each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')
