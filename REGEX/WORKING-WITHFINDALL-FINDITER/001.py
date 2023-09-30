#!/usr/bin/python3.10
import re
text="This is a python and we are having python2 and python3 version"
my_pat=r'\bpython[23]?\b' #?= one or none.
print(re.match(my_pat,text)) #Match will check in the 0th index only.
print(re.search(my_pat,text)) #Search will into the entire string.
print(re.findall(my_pat,text)) #Findall will match all the pattern.
print(len(re.findall(my_pat,text))) #Findall will match all the pattern with lenth.

print("===========Finditer===========")
my_pat1=r'\bpython[23]?\b'
for each_ob in re.finditer(my_pat1,text):
    print("-------------")
    print(each_ob)
    print(f'The match is: {each_ob.group()} starting index: {each_ob.start()}, ending index {each_ob.end()-1}')

