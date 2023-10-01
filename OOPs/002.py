#!/usr/bin/python3.10
import os
class Tomcat: #instead of self you use any word.
    def get_details_for_each_test(self,file):
        self.tcf=file
        self.th=os.path.dirname(os.path.dirname(file))
        return None

    def display_details(self):
        print(f"The test file is: {self.tcf}\n The tomcat home is: {self.th}")
        return None

def main():
    test1=Tomcat()
    test2=Tomcat()

    test1.get_details_for_each_test("/root/PYTHON/OOPs/test1/file.txt")
    #get_details_for_each_test
    test2.get_details_for_each_test("/root/PYTHON/OOPs/test2/file.txt")
    test1.display_details()
    test2.display_details()

    return None

if __name__=="__main__":
    main()
