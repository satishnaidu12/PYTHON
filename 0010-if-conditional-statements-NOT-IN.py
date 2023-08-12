#!/usr/bin/python3.10
num=eval(input("Enter any number between 1-10 range: "))
num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if num in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(num))
else:
    print(f'{num} is not in 1-10 range')
