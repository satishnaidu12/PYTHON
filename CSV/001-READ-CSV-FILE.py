#!/usr/bin/python3.10
import csv
req_file=("/home/satish/test/info.csv")

'''
fo=open(req_file,"r")
content=fo.readlines()
fo.close()

for each in content:
    print(each.strip("\n"))
'''
fo=open(req_file,"r")
data=csv.reader(fo)

for each in data:
    print(each)
fo.close()
