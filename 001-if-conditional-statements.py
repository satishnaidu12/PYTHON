#!/usr/bin/python3.10
import os
t_w=os.get_terminal_size().columns
given_str=input("ENter your strings: ")
print(given_str)
usr_cnf=input("DO you want to allign text: say yes or no? ")
if usr_cnf=="yes":
    print(given_str.center(t_w).title())
    print(given_str.ljust(t_w).title())
    print(given_str.rjust(t_w).title())
