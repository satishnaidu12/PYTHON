#!/usr/bin/python3.10
import csv
req_file=("/home/satish/test/new_info.csv")

'''
fo=open(req_file,"r")
content=fo.readlines()
fo.close()

for each in content:
    print(each.strip("\n"))
'''
fo=open(req_file,"r")
data=csv.reader(fo,delimiter="|")
#print(list(data))
print(f'The header is:\n {list(data)[0]}')
fo.close()
