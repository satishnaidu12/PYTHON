#!/usr/bin/python3.10
paths=["/usr/bin", "/usr/bin/httpd", "/home/satish/test"]
for each_path in paths:
    print("Now working on: ",each_path)
    if "test" in each_path:
        print (each_path)
        break
print("Outside of for loop")
