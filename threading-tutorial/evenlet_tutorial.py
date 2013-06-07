'''
Created on Jun 6, 2013

@author: shengjiemin
'''
import thread
from eventlet import tpool
from eventlet import GreenPool

def my_func(start_ident):
    print "start_ident:%s" % start_ident
    print "running in new thread: %s %s" % (start_ident != thread.get_ident(), 
                                            thread.get_ident())

tpool.execute(my_func, thread.get_ident())


def worker(line):
    print "worker in thread %s" % thread.get_ident()
    return line

pool = GreenPool()
for result in pool.imap(worker, open("test.txt", 'r')):
    print result
