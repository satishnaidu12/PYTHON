#!/usr/bin/python3.10
import csv
req_file=("/home/satish/test/create_info.csv")

#PYTHON2
#fo=open(req_file,"wb")
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['S_No',"Name","Age"])
csv_writer.writerow(['1',"Sat","35"])
fo.close()
