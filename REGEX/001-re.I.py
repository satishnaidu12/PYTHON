#!/usr/bin/python3.10
import re
text="this is a string This is a new starting THIS"
my_pat=r"this"
print(re.findall(my_pat,text))
print(re.findall(my_pat,text,re.I))           #IGNORE CASE sensitive
print(re.findall(my_pat,text,re.IGNORECASE))  #IGNORE CASE sensitive

print("%%%%%%%%%%%%%%%%%%%%%%%")
text1="""this is a string
This is second line
this is third line
asdedf this"""

my_pat1=r'this'
my_pat2=r'^this'
print(re.findall(my_pat1,text1))             #Print all this.
print(re.findall(my_pat1,text1,re.M))        #Print all this.

print(re.findall(my_pat2,text1))             #Print starting "this" from 1st line even though "this" is present in multiple that too in starting of the line.

print(re.findall(my_pat2,text1,re.M))        #Print all "this" which starts in each line with casesentive

print(re.findall(my_pat2,text1,re.M|re.I))   #Print all "this" which starts in each line with ignorecasesensitive

print("################################")

text2="""this is a string EnD
This is second line END
this is third line end
asdedf this end"""

my_pat3=r'end'
my_pat4=r'end$'
print(re.findall(my_pat3,text2))                    #Print all end.
print(re.findall(my_pat3,text2,re.M))


print(re.findall(my_pat4,text2))                    #Print all "end" which is in end of the line.
print(re.findall(my_pat4,text2,re.M))               #Print all "end" which is in end of the each multiple line with case sensitive.
print(re.findall(my_pat4,text2,re.M|re.I))               #Print all "end" which is in end of the each multiple line with IGNORECASESENSITIVE.

