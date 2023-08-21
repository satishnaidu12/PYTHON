#!/usr/bin/python3.10
sfile=input("ENTER your source file: ")
dfile=input("Enter your destination file: ")
sfo=open(sfile,"r")
content=sfo.read()
sfo.close()

dfo=open(dfile,"w")
dfo.write(content)
dfo.close()
