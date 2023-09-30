#!/usr/bin/python3.10
import re
text="This is my ip of a db server: 255.100.102.103 2345672345678956234567"
#my_pattern="\d\d\d"
#my_pattern="\d\d\d.\d\d\d.\d\d\d.\d\d\d" #It doesn't matches the dot.
my_pattern="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d" #It matches the dot with dot.
print(re.findall(my_pattern,text))
