#!/usr/bin/python3.10
x=3>4
print(x)
y=1 in [3,4,5]
print(y)

z=3>4 and 1 in [3,4,5]
print(z)

a=3<4 and 1 not in [3,4,5]
print(a)

#In AND  logical operators all should be true, even if 1 is false all will be false, please b and b1 example.
b=1<2 and 2<3 and 3<4
print(b)

b1=1>2 and 2<3 and 3<4
print(b1)


