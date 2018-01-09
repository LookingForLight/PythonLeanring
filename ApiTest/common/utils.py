#-*-coding:utf-8-*-
import yaml
import os

yaml_path = []

def load_yaml_file(yaml_file):

	with open(yaml_file,'r') as content:
		yaml_name = os.path.basename(yaml_file)
		yaml_path.append(yaml_name)
		return yaml.load(content)

def load_testcases(case_file_path):

	file_postfix = os.path.splitext(case_file_path)[1]

	if file_postfix == '.yml':
		return load_yaml_file(case_file_path)
	else:
		raise ValueError("文件名后缀不正确")

def parse_testcase(case_file_path):
	test_info ={
		"testcase": []
	}

	case_list = load_testcases(case_file_path)

	for item in case_list:
		for key in item:
			if key == 'test':
				test_info['testcase'].append(item['test'])
	return [test_info]

test_list = parse_testcase("../testcase/democase.yml")
print test_list