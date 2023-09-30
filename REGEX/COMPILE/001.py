#!/usr/bin/python3.10
import re
text="This is about python. Python is easy to learn and we have two major versions: python2 and python3."
my_pat=r"\bPython[23]?\b"
print(re.findall(my_pat,text))
print(re.findall(my_pat,text,flags=re.I))

print("=======================")
print(re.search(my_pat,text))
print(re.search(my_pat,text,flags=re.I))

print("=============================")
print(re.split(my_pat,text))

print("============END OF RE MODULE============")
print("============pattern object============")

pat_ob=re.compile(my_pat,flags=re.I)
print(pat_ob)
print(pat_ob.search(text))
print(pat_ob.findall(text))

#Same pattern in different places in your script, you can use compile operation.
