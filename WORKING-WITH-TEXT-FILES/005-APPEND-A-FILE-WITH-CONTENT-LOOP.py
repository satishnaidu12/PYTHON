#!/usr/bin/python3.10
my_content=["This is using loop-iteration-1","This is using loop-iteration-2","This is using loop-3"]

fo=open("with_loop.txt","a")

for each_line in my_content:
    fo.write(each_line+"\n")
fo.close()
