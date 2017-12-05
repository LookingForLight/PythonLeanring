#-*-coding:utf-8-*-
"""
test
"""


class MyClass (object):

	count = 0

	def __init__(self,name,sex):

		self.name = name
		self.sex = sex
		# print "调用了父类的构造函数"

	def show_info(self):
		print "调用父类方法"
		print "my name is %s,sex is %s" % (self.name, self.sex)

p = MyClass("zhulei","man")
#
p.show_info()
# print p.name, p.sex
#
# print MyClass.__dict__
# print p.__dict__
# print MyClass.__name__


class MyStudent (MyClass):

	def __init__(self, name,sex,age, homeland):

		MyClass.__init__(self,name,sex)
		self.age = age
		self.homeland = homeland

		print "调用了派生类的构造函数"


	def show_sinfo(self):
		print "在派生类中调用父类方法"
		print MyClass.show_info(self)
		# print "my age is %d,homeland is %s" % (self.age, self.homeland)

#实例化子类
s = MyStudent("zhulei","man",18,"suzhou")

# s.show_info()
s.show_info()
s.sex = "sman"

s.show_info()
o
class Student2(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):

		if not isinstance(value,int):
			raise ValueError("score must be interge")
		if value < 0 or value > 100:
			raise ValueError("score must between 0~~100")
		self._score = value
stu = Student2()
stu._score = 99
print stu._score