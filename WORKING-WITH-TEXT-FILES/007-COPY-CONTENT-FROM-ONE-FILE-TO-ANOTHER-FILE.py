#!/usr/bin/python3.10
sfile="/root/PYTHON/WORKING-WITH-TEXT-FILES/file1.txt"
dfile="file2.txt"
sfo=open(sfile,"r")
content=sfo.read()
sfo.close()

dfo=open(dfile,"w")
dfo.write(content)
dfo.close()
