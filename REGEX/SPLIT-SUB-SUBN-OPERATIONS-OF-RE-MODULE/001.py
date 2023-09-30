#!/usr/bin/python3.10
import re
#help(re.split)
print("----------------------------")
text="This is about Python python and python is very easy and we are having python2 vers and Python3 vers"
my_pat=r'python'

print(re.split(my_pat,text))
my_pat1=r'python[23]?'

print(re.split(my_pat1,text,flags=re.I))


print("------MAXSPLIT=0----------")
print(re.split(my_pat1,text,maxsplit=0,flags=re.I))

print("------MAXSPLIT=1----------")
print(re.split(my_pat1,text,maxsplit=1,flags=re.I))

print("------MAXSPLIT=2----------")
print(re.split(my_pat1,text,maxsplit=2,flags=re.I))

#Substitue python with jython
print(re.sub(my_pat,'jython',text,flags=re.I))

new_text=re.sub(my_pat,'jython',text,flags=re.I)

print(new_text)
