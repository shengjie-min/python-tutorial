'''
Created on Mar 17, 2013

@author: shengjiemin
'''
import abc
from test.test_macos import TestMacOS

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
    
    def test_parent2(self):
        "no implementation still"
        
#if __name__ == '__main__':
#    print "main..."
#    SubClass().test_parent1()
#    ABCClass()
    
class TestM(object):
    
    def __init__(self, auth_token=None, user=None, tenant=None, is_admin=False,
                 read_only=False, show_deleted=False, request_id=None):
        print auth_token
        print user
        print tenant
        print is_admin

TestM('admin', 'admin', is_admin=True)