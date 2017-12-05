# -*- coding: UTF-8 -*-
import json
import demjson
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)
emp1.displayCount();
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
    def count2(self):
        print self.__secretCount

counter = JustCounter()
counter.count()
# 在类的对象生成后,调用含有类私有属性的函数时就可以使用到私有属性.
counter.count()
#第二次同样可以.
print counter.publicCount
print counter._JustCounter__secretCount  # 不改写报错，实例不能访问私有变量
try:
    counter.count2()
except IOError:
    print "不能调用非公有属性!"
else:
    print "ok!" #现在呢!证明是滴!

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print json

text = demjson.decode(json)
print  text