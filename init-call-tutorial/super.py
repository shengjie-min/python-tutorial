'''
Created on Mar 18, 2013

@author: shengjiemin
'''
class Base(object):
    def __init__(self, a):
        print "Base created" + a + "\n"
class Base2(object):
    def __init__(self, a):
        print "Base2 created" + a + "\n"

class ChildA(Base):
    def __init__(self, b):
        Base.__init__(self, "test3")

class ChildB(Base2, Base):
    def __init__(self):
        print "\n ========= \n"
        super(ChildB, self).__init__("test4")

print ChildA("test1"),ChildB()

