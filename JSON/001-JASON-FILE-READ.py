#!/usr/bin/python3.10
import json
req_file="/root/PYTHON/CSV/001-file.json"
fo=open(req_file,'r')
print(json.load(fo))
fo.close()
