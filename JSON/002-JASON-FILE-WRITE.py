#!/usr/bin/python3.10
import json
my_dict={'Name':'Narendra','skills':['Python','shell','yaml','aws']}

req_file="/root/PYTHON/JSON/002-file.json"

fo=open(req_file,'w')

#json.dump(my_dict,fo)

json.dump(my_dict,fo,indent=4)

fo.close()
