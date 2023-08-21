#!/usr/bin/python3.10
import subprocess
cmd="java -version"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
if rc==0:
    print(o)
else:
    print(e)
