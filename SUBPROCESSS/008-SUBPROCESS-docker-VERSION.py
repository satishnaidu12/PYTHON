#!/usr/bin/python3.10
import subprocess
cmd=['docker', 'version']
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()

if not rc==0:
   #print("output is: ", o)
   for each_line in o.splitlines():
    if "Version" in each_line:
       print(each_line.split()[1])

