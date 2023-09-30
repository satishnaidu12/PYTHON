#!/usr/bin/python3.10
import re
text="it is a python and \n    itlearnis   easy    to learn"
#text="itis is a python and it is easy to learn"
#my_pat="i[ts]"
#my_pat="^i[ts]"
my_pat="^i[st]" #starting string
my_pat1="learn$" #Ending string
my_pat2="\\blearn" #Print the if there is space in left of the given word.
my_pat3=r"\blearn" # please r=raw string if you don't want to escape character.
my_pat4=r"\Blearn\B" # please r=raw string if you don't want to escape character.
my_pat5=r"\t"       #Print tab
my_pat6=r"\n"       #Print newline
print(re.findall(my_pat,text))
print(re.findall(my_pat1,text))
print(re.findall(my_pat2,text))
print(re.findall(my_pat3,text))
print(re.findall(my_pat4,text))
print(re.findall(my_pat5,text))
print(re.findall(my_pat6,text))
