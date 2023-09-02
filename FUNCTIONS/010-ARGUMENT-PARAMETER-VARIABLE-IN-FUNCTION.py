#!/usr/bin/python3.10
'''
def get_add():
    aresult=a+b
    print(f"The addition of {a} and {b} is: {aresult}")
    return None
def get_sub():
    sresult=a-b
    print(f"The subtraction of {a} and {b} is: {sresult}")
def main():
    a=eval(input("Enter your first num: "))
    b=eval(input("Enter your second num: "))
    return None
main()
    
'''
'''
def get_add(a,b): #Positional Parameters
    aresult=a+b
    print(f"The addition of {a} and {b} is: {aresult}")
    return None
def get_sub(a,b): #Positional Parameters
    sresult=a-b
    print(f"The subtraction of {a} and {b} is: {sresult}")
    return None
def main():
    a=eval(input("Enter your first num: "))
    b=eval(input("Enter your second num: "))
    get_add(a,b)
    print("In Sub traction a value is assinged to b and b value is assinged to a")
    get_sub(b,a) #Arguments
    return None
main()
'''
'''
def get_add(p,q): #Positional Parameters
    aresult=p+q
    print(f"The addition of {p} and {q} is: {aresult}")
    return None
def get_sub(m,n): #Positional Parameters
    sresult=m-n
    print(f"The subtraction of {m} and {n} is: {sresult}")
    return None
def main():
    a=eval(input("Enter your first num: "))
    b=eval(input("Enter your second num: "))
    print("In Add a value is assinged to p and b value is assinged to n")
    get_add(a,b)
    print("In Sub traction a value is assinged to m and b value is assinged to n")
    get_sub(a,b) #Arguments
    return None

main()
'''

def get_add(p,q): #Positional Parameters
    aresult=p+q
    print(f"The addition of {p} and {q} is: {aresult}")
    return None
def get_sub(m,n): #Positional Parameters
    sresult=m-n
    print(f"The subtraction of {m} and {n} is: {sresult}")
    return None
def main():
    #get_sub(9,10) #Arguments
    x=10
    get_sub(9,x) #Arguments
    return None

main()
