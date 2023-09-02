#!/usr/bin/python3.10
import csv
req_file=("/home/satish/test/create_info.csv")

#PYTHON2
#fo=open(req_file,"wb")
#PYTHON3
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
data=(['S_No',"Name","Age"],['1',"Sat","35"])
csv_writer.writerows(data)
fo.close()
