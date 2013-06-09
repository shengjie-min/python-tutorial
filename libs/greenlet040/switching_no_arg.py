'''
Created on Jun 9, 2013

@author: shengjiemin


greenlet: Lightweight in-process concurrent programming
'''
from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()