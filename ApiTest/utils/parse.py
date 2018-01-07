#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

"""
@author:stone.z
"""


def load_testcases(case_file_path):

	with open(case_file_path, 'r') as result:

		content = yaml.load(result)
		request_data = content['-test'].get("request")

		return request_data
