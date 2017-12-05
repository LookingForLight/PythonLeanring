#-*-coding:utf-8-*-
#交换两个变量值
a = 1
b = 2
tmp = a
a = b
b = tmp
print  a,b

c = 4
d = 5
c, d = d, c
print c,d

#真值判断
attr = False
if attr:
	print "true"
else:
	print "false"
#空值判断
list =[1]
if list:
	print "not empty"
else:
	print "empty"

#字符串连接
names = ['zhulei','dt','yxj','hq','yjk']
s = names[0]
for name in names:
	s+=','+name
print s


print ','.join(names)

print sum(i*2 for i in range(10))


for name in names:
	print name
#反向遍历
for name in reversed(names):
	print name

#有序遍历
print "----------有序遍历-------"
for name in sorted(names,reverse=True):
	print name
#同时遍历两个list

list_a = ['a','b','c','d']
list_b = [1,2,3]
list_c ={}
for key,value in zip(list_a,list_b):
	print key,value

dict_a = {"a1":"1","b1":'2',"c1":'3'}

for k,v in dict_a.items():
	print k,v

for k,v in dict_a.iteritems():
	print k,v

d ={}
for value in names:
	d[value] = d.get(value,0)+1

dic = {}
for name in names:
	key =len(name)
	dic.setdefault(key,[]).append(name)
print dic