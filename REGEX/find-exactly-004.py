#!/usr/bin/python3.10
import re
text="This is a pythonnnn and aaaa xyzaaa python xz xaz aaz xaaaaaz xaaaaz"
my_pat=r"\bpython{4}\b"  #four times n
my_pat1=r"\ba{4}\b"      #four times n
my_pat2=r"\bxyza{3}\b"      #four times n
my_pat3=r"\bxa{2,4}z\b"      #Exactly two and and 4 times a
my_pat4=r"\bxa{2,}z\b"      #Exactly two or more than 2 times.
my_pat5=r"\bxa+z\b"      # A one more time
my_pat6=r"\bxa{1,}z\b"    # A one more time
my_pat7=r"\bxa*z\b"    # zero times or many times
my_pat8=r"\bxa?z\b"    # a? means one time or zero time
print(re.findall(my_pat,text))
print(re.findall(my_pat1,text))
print(re.findall(my_pat2,text))
print(re.findall(my_pat3,text))
print(re.findall(my_pat4,text))
print(re.findall(my_pat5,text))
print(re.findall(my_pat6,text))
print(re.findall(my_pat7,text))
print(re.findall(my_pat8,text))
