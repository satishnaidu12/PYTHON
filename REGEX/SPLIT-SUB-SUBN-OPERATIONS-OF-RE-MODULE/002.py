#!/usr/bin/python3.10
import re
#help(re.split)
print("----------------------------")
text="This is about Python python and python is very easy and we are having python2 vers and Python3 vers"
my_pat=r'\bpython\b'
my_pat1=r'\b[pP]ython\b'


print(re.findall(my_pat,text))
print(re.findall(my_pat,text,flags=re.I))
print(re.findall(my_pat1,text))
