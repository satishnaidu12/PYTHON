#!/usr/bin/python3.10
num=eval(input("Enter any number between 1-10 range: "))
if num in [1,2,3,4,5,6,7,8,9,10]:
    if num==1:
        print("one")
    elif num==2:
        print("two")
    elif num==3:
        print("three")
    elif num==4:
        print("four")
    elif num==5:
        print("five")
    elif num==6:
        print("six")
    elif num==7:
        print("seven")
    elif num==8:
        print("Eight")
    elif num==9:
        print("Nine")
    else:
        print("ten")
else:
    print(f'{num} is not in 1-10 range')
