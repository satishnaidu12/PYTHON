#!/usr/bin/python3.10
import os
import sys
import datetime
req_path=input("Enter your path:"  )
age=1
if not os.path.exists(req_path):
    print("Please provide valid path ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide a directory path")
    sys.exist(2)
today=datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
       file_creation_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
       dif_days=(today-file_creation_date).days
       if dif_days > age:
           print(each_file_path,dif_days)
    
