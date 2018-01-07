#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parse
"""
@author:stone.z
"""

request_data = parse.load_testcases("../testcase/democase.yml")
print  request_data.get('url')
print  request_data.get('method')
print  request_data.get('header')
print  request_data.get('body')