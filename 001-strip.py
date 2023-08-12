#!/usr/bin/python3.10
x="   python "
print(x.strip())

#Remove last letter or last letter.
x="python"
print(x.strip('n'))
#Remove 1st letter or last letter.
x="python"
print(x.strip('p'))

#Remove last word 
x="Python scripting is hard"
print(x.strip('hard'))

#Remove 1st word.
x="Python scripting is hard"
print(x.strip('Python'))
