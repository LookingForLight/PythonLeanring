
# -*- coding: UTF-8 -*-
from operator import itemgetter

def printme( str ):

    "print string to sreen"
    print str
    return

printme('ddd')

def ChangeInt( a ):
    a = 10

b=2
a=1
ChangeInt(b)
print b
print a


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

kw = {'city': 'Beijing', 'job': 'Engineer'}
def person(name,age,**kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)

person('Michael', 30,**kw)

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=33)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print key

for value in d.itervalues():
    print value


L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))