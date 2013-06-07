'''
Created on Mar 18, 2013

@author: shengjiemin
'''

class Constructor:
    def __init__(self, a):
        print "__init__ called"
        
    def __call__(self):
        print "__call__ called"
    
    def dummy(self):
        print "a dummy method called"

print "creating x obj"
x = Constructor(1)
print "calling x object"
x()
print "calling dummy method"
x.dummy()