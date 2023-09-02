#!/usr/bin/python3.10
#Interviewi: How we can pass arguments to your called function based on your key words.
def display(a,b):
    print(f'a={b}')
    return None
display(3,4)
display(a=3,b=4)
display(b=4,a=3)
