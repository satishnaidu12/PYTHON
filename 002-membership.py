#!/usr/bin/python3.10
'''
x=[4,5,6,3,7,9]
print(6 in x)
print(1 in x)
'''
##### Java availble or not
valid_java=['1.4','1.5','1.6','1.7']
host_java=['1.8']

if host_java in valid_java:
    print("host deployed of valid java")
else:
    print("host deployed of invalid java")
