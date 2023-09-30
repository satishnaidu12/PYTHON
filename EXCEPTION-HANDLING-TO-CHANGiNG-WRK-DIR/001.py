#!/usr/bin/python3.10
import os
'''
req_path=input("Enter path to CHN wrk dir: ")
print("The current wrk dir is: ", os.getcwd())
try:
    os.chdir(req_path)
    print("Now your new wrk dir is: ",os.getcwd())
except FileNotFoundError:
    print("Given path is a file path. So can't chn working dir")
except NotADirectoryError:
    print("Sorry you don't have access for the given path. so can't chn wrk dir")
except Exception as e:
    print(e)
'''

def main():
    req_path=input("Enter path to CHN wrk dir: ")
    print("The current wrk dir is: ", os.getcwd())
    try:
        os.chdir(req_path)
        print("Now your new wrk dir is: ",os.getcwd())
    except FileNotFoundError:
        print("Given path is a file path. So can't chn working dir")
    except NotADirectoryError:
        print("Sorry you don't have access for the given path. so can't chn wrk dir")
    except Exception as e:
        print(e)
    return None

if __name__=="__main__":
    main()
