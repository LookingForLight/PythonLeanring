#-*-coding:utf-8-*-

import requests
import json
"""
@author:朱磊

"""

class ParseContext(object):

	result = {"SrcNotExistKey": [], "DstNotExistKey": [], "NotSameValue": []}

	def __init__(self, url):
		self.url = url

	@property
	def url(self):

		return self._url

	@url.setter
	def url(self,value):

		if not isinstance(value,str):
			raise ValueError("url must be string")
		if value.startswith('http:'):
			self._url = value
		else:
			raise ValueError("url only can handler the url start with http now")

	#解析返回值函数
	def resData(self):
		try:
			req = requests.get(self.url)
			req.encoding = 'utf-8'
		except requests.exceptions.requestException,e:
			print "请请求类异常",e.message
		finally:
			pass

		if req.status_code == 200:
			return req.json()
		else:
			raise ValueError("can not parse data")

	@classmethod
	#递归方法
	def compareResult(cls, src_data, dst_data):
		#若为dict数据
		if isinstance(src_data,dict):
			for key in src_data:
				if key not in dst_data:
					#print "dst 不存在key值：",key
					cls.result["DstNotExistKey"].append(key)
			for key in dst_data:
				if key in src_data:
					#递归调用
					ParseContext.compareResult(src_data[key],dst_data[key])
				else:
					#print "scr 不存在key值：",key
					cls.result["SrcNotExistKey"].append(key)
		#若是list
		elif isinstance(src_data,list):
			if len(src_data)!=len(dst_data):
				print "src_data length is %d,dst_data length is %d",(len(src_data),len(dst_data))
			for src, dst in zip(src_data,dst_data):
				#递归调用
				ParseContext.compareResult(src, dst)
		else:
			if str(src_data)!=str(dst_data):
				#print "不同的值：",src_data
				cls.result["NotSameValue"].append(src_data)
		#返回unicode数据类型
		return json.dumps(cls.result,encoding='utf-8',indent=4,ensure_ascii=False)


urldemo = "http://10.101.52.94:5008/api/get_json_data"

pc = ParseContext(urldemo)

dict1 = pc.resData()
dict2 = pc.resData()
print dict1
print dict2
result = ParseContext.compareResult(dict1,dict2)
print result

