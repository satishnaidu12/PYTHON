#!/usr/bin/python3.10
import re
text="""This is for python
and there are two major vers 
python2 and python3
in future python4"""

print("==================Match============")
my_pat=r'\bpython\b'
my_pat1=r'\bpython[23]\b'
print(re.findall(my_pat,text))
print(re.findall(my_pat1,text))

print("============SEARCH========")
search_object=re.search(my_pat,text)

if search_object:
    print("match from ur pattern: ",search_object.group())
    print("Starting index: ",search_object.start())
    print("Ending index: ",search_object.end()-1)
    print("Length index: ",search_object.end()-search_object.start())
else:
    print("No match found")



print("====================")
print("Difference between match and search is: search will look into entire line and will find only the 1st match, MATCH will look into 0th postion sinlgle or multiline, even you tru forcefully it will not work, but ignore case")
