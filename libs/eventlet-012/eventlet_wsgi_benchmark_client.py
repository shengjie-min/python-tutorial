'''
Created on June 9, 2013

@author: shengjiemin

To test the difference,
1. run eventlet_wsgi server
2. run this wsgi_benchmarking client

with httplib2:
    watch --inteval=1 'sudo netstat -a | grep '50010''
    will only indicate there is one socket connection at time working which 
    blocks other green threads
with monkey_patched httplib2
    will indicate there are 10 non-blocking socket connections asynchronously

import httplib2 directly, httplib2 doesn't natively support cooperative 
yielding. 

monkey_patch httplib2 will make httplib2 green.
'''

from eventlet.greenpool import GreenPool
import eventlet
import random

import httplib2

# uncomment this line to green httplib2
# httplib2 = eventlet.import_patched('httplib2')

def worker(url):
    print "worker "+str(random.random())
    h = httplib2.Http()
    resp, content = h.request(url, "GET")
    return resp


pool = GreenPool(size=10)
results = pool.imap(worker, open("urls.txt", 'r'))

for result in results:
    print result
print "done...."
pool.waitall()
