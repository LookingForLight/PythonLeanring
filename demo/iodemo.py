# -*- coding: UTF-8 -*-


import re
import json
import requests

url = "http://10.101.52.94:5008/api/get_json_data"

req = requests.get(url)
req.encoding = "utf-8"
print "httpcode:",req.status_code
#返回python对象dict
# data1 = req.json()
data2 = req.json()
# print type(data1), data1
print type(data2), data2
# data1_encode = unicode.encode(data1)
python_to_json = json.dumps(data2,ensure_ascii=False,indent=4)
# print data1_encode
print python_to_json,type(python_to_json)
# json_data=json.dumps(data,indent=4,separators=(',',":"),ensure_ascii=False)
# print type(json_data)
json_to_python = json.loads(python_to_json)
print type(json_to_python)
for k, v in json_to_python.iteritems():
	print k,"--->",k



