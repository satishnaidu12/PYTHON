#!/usr/bin/python3.10
#import os
'''
req_path=("/home/satish/test")
all_f_ds=os.listdir(req_path)
for each_file in all_f_ds:
    if each_file.endswith(".lock"):
        print(each_file)
'''
import os
import sys
import datetime
today=datetime.datetime.now()
age=1
req_path=("/home/satish/test/")
all_f_ds=os.listdir(req_path)
for each_file in all_f_ds:
    if each_file.endswith(".txt"):
            each_file_path=os.path.join(req_path,each_file) 
            creation_time=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
            dif_days=(today-creation_time).days
            if dif_days > age:
                print(each_file_path,dif_days)
                #fo=open("demowrite.txt","w")
                #fo.write("This a first line\nThis is second line\n")
                #fo.close()
