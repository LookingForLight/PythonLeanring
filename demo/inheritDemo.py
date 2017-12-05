# -*- coding: UTF-8 -*-

class Animal(object):

    def running(self):
        print "running"


class dog(Animal):
    def running(self):
        print "dog is running"

class cat(Animal):
    def running(self):
        print "cat is running"


dog1 =dog()
dog1.running();

cat1 =cat()
cat1.running();

a = list() # a是list类型
b = Animal() # b是Animal类型


print isinstance(a, list)
print isinstance(b, Animal)

def run_twice(animal):
    animal.running()
    animal.running()


run_twice(dog())