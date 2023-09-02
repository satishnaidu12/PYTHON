#!/usr/bin/python3.10
import os
import time
import platform

'''
#Without function
if platform.system()=="Windows":
    print("Please wait. Cleaning the screen....")
    time.sleep(2)
    os.system("cls")
    print("Please wait finding the list of dir and files")
    time.sleep(2)
    os.system("dir")
else:
    print("Please wait. Cleaning the screen....")
    time.sleep(2)
    os.system("clear")
    print("Please wait finding the list of dir and files")
    time.sleep(2)
    os.system("ls -lthr")
'''

#WITH FUNCTION
def mycode(cmd1,cmd2):
    print("Please wait. cleaning the screen....")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait finding the list of dir and files")
    time.sleep(2)
    os.system(cmd2)
if platform.system()=="Windows":
    mycode("cls","dir")
else:
    mycode('clear','ls -lthr')
