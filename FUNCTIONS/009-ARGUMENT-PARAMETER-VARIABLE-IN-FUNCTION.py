#!/usr/bin/python3.10
'''
num=eval(input("Enter your number: "))
result=num+1
print(f"your result is: {result}")o
'''

'''
def get_result():
    result=num+1
    print(f"your result is: {result}")
    return None
def main():
    num=eval(input("Enter your number: "))
    get_result()
    return None
main()
'''
'''

def get_result():
    result=num+1
    print(f"your result is: {result}")
    return None
def main():
    global num
    num=eval(input("Enter your number: "))
    get_result()
    return None
main()
'''
'''
def get_result(value):
    result=num+1
    print(f"your result is: {result}")
    return None
def main():
    num=eval(input("Enter your number: "))
    get_result(num)
    return None
main()
'''
def get_result(value): #parameter/positional argumernts
    result=value+1
    print(f"your result is: {result}")
    return None
def main():
    num=eval(input("Enter your number: "))
    get_result(num) #Arguments
    return None
main()
