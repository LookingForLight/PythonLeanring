
# -*- coding: UTF-8 -*-
import time
import calendar
import datetime
import funcation

# 格式化成2016-03-20 11:45:39形式
timestamp=time.time();
print "timestamp",timestamp
print type(time.time())
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sec))

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;


i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

funcation.changeme([1,2,3,4])

fo = open("foo.txt", "wb")
fo.write( "www.runoob.com!\nVery good site!\n");
position = fo.tell();
print "当前文件位置 : ", position
fo.close();
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace