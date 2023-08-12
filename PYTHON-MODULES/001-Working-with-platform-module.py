#!/usr/bin/python3.10
import platform as pt
print(f"This is {pt.system()} os")
print(f'Python version is: {pt.python_version()}')
print(f'Python version is: {pt.python_version_tuple()}')
print(pt.machine())
print(pt.release())
print(pt.platform())
print(pt.processor())
print(pt.architecture())
print(pt.node())
print(pt.uname())
