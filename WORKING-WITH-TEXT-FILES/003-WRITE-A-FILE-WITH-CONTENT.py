#!/usr/bin/python3.10
my_content=["This is a line-1\n","This is a line-2\n","This is a data-3\n"]
fo=open("conent.txt","w")
fo.writelines(my_content)
fo.close()
