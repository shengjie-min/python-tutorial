'''
Created on May 23, 2013

@author: shengjiemin
'''


class parent(object):

    def try_this(self):
        print "I am the parent"


class kid_hasbody(parent):
    print "I am the kid"

class kid_nobody(parent):
    pass

kid_hasbody().try_this()
print "=============="
kid_nobody().try_this()