#!/usr/bin/python3.10
import re
text="This is about python. Python is easy to learn and we have two majpr versuibs: python2 and python3"

my_pat=r'\bPython[23]?\b'

print(re.search(my_pat,text))
print(re.findall(my_pat,text,flags=re.I))
