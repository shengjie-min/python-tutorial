'''
Created on May 23, 2013

@author: shengjiemin


Multi-Inheritance rule:

This is depth-first, left-to-right. Thus, if an attribute is not found in
DerivedClassName, it is searched in Base1, then (recursively) in the base
classes of Base1, and only if it is not found there, it is searched in Base2,
and so on.
'''


class Father(object):
    print "[Father Class says: ] I am the father class"
    def __init__(self):
        print "[Father Object says: ] I am the father object"
    def try_this(self):
        print "[Father method says: ] father try_this()"


class Mother(object):
    print "[Mother Class says: ] I am the mother class"
    def __init__(self):
        print "[Mother Object says: ] I am the mother"
    def try_this(self):
        print "[Mother method says: ] mother try_this()"


class KidHasFather(Father):
    print "[KidHasFather class says: ] I am the kidhasfather"
    def __init__(self):
        print "[KidHasFather Object says: ] I am the kidhasfather"


class KidHasBothParents(Father, Mother):
    print "[KidHasBothParents class says: ] I am the kidhasbothparents"
    def __init__(self):
        print "[KidHasBothParents Object says: ] I am the kidhasbothparents"

KidHasFather().try_this()
print "=================="
KidHasBothParents().try_this()


