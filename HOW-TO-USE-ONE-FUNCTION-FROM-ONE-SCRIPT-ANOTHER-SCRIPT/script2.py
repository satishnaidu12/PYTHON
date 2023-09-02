#!/usr/bin/python3.10
import script1
print(dir(script1)) #To know the available function.
def mult(a,b):
    print(f'The multiply of {a} and {b} is {a*b}')
    return None
def main():
    x=10
    y=20
    script1.addition(x,y)
    return None
if __name__=="__main__":
    main()

