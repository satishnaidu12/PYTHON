#!/usr/bin/python3.10
import os
t_w=os.get_terminal_size().columns

given_str=input("ENTER your string: ")
print(given_str.center(t_w).title())
print(given_str.ljust(t_w).title())
print(given_str.rjust(t_w).title())

