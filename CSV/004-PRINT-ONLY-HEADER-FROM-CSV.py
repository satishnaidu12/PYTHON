#!/usr/bin/python3.10
import csv
req_file=("/home/satish/test/new_info.csv")

fo=open(req_file,"r")
data=csv.reader(fo,delimiter="|")
header=next(data)
#print("The header is: ",header)
print("The no of rows are: ",len(list(data))-1)
fo.close()
