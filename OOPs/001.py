#!/usr/bin/python3.10
import os
def get_details_for_each_test(file):
    tcf=file
    th=os.path.dirname(os.path.dirname(file))
    print(f"The test file is: {tcf}\n the test home is: {th}")
    return None

def main():
    test1="/root/PYTHON/OOPs/test1/file.txt"
    test2="/root/PYTHON/OOPs/test2/file.txt"
    get_details_for_each_test(test1)
    get_details_for_each_test(test2)
    return None

if __name__=="__main__":
    main()
