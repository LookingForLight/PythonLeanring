#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

"""
@author:stone.z
"""


def load_testcases(case_file_path):

	with open(case_file_path, 'r') as result:

		content = yaml.load(result)
		request_data = []
		if content:

			for index,value in enumerate(content):

				request = value['test'].get('request')
				name = value['test'].get('name')
				request_data.append(request)


			return request_data
		else:
			raise ValueError("can not empty")


# with open("../testcase/democase.yml", 'r') as result:
#
# 	content = yaml.load(result)
# 	print content
# 	print type(content)
# 	print len(content)
# 	request_data = []
# 	for index , value in enumerate(content):
# 		request = value['test'].get('request')
# 		request_data = request_data.append(request)

