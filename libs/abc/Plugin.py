'''
Created on Mar 17, 2013

@author: shengjiemin
'''
import abc

class ABCClass(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def test_parent1(self):
        """a parent class method for testing"""
    
    @abc.abstractmethod
    def test_parent2(self):
        """a parent class method for testing"""
    
class SubClass(ABCClass):

    def test_parent1(self):
        print 'implementation is here!'

#     def test_parent2(self):
#         "no implementation still"

if __name__ == '__main__':
    print "main..."
    SubClass().test_parent1()
#     SubClass().test_parent2()
#     ABCClass()