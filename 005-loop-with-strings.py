#!/usr/bin/python3.10
my_list=[3,23,34,5,67,89,23]
for each in my_list:
    rem=each%2
    if rem==0:
        print(f"{each} is even")
    else:
        print(f"{each} is odd")
