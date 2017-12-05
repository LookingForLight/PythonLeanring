# -*- coding: UTF-8 -*-

def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

print calc_sum(1,2,3,4,5)


def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax+=n
        return ax
    return sum


f=lazy_sum(1,2,3,4,5,6)
print f
print f()

class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print ('%s:%s'%(self.name,self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()