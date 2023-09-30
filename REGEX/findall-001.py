#!/usr/bin/python3.10
import re
'''
text="This is @ python and it is eacy to learn"
#my_pattern="is"
#my_pattern="i[st]"
#my_pattern="x"
#my_pattern="a"
#my_pattern="[@an]"
#my_pattern="\w"
#my_pattern="\w\w"
my_pattern="\w\w\w"
print(re.findall(my_pattern,text))
'''
'''
text="This is 45 @ python2 python3 and it is eacy to learn"
#my_pattern="python2"
#my_pattern="python\d"
my_pattern="\d\d"
print(re.findall(my_pattern,text))
'''
text="This is 45 @ python2 python3 and it is eacy to learn."
#my_pattern="."
#my_pattern=".."
#my_pattern="..."
my_pattern="\." #Matches dot with dot
print(re.findall(my_pattern,text))
