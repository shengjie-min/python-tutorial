'''
Created on Jun 8, 2013

@author: shengjiemin

This is a comparison among running count() method in:
1. subsequential order
2. native threads
3. green threads

Results:
green threads > subsequential order > native threads

because native threads on multi-cores are deadly slow:
    - GIL
    - context-switching
    - consumes more memory
    - creation over-head

green threads are quick:
    - no creation over-head, very light-weight
    - cooperative yielding, no context-switching, deterministic(you control
      the order, who runs first, who runs next)
    - limited to one core/processor
'''
import datetime
import time
import threading
from eventlet import GreenPool


def count():
    for i in range(100000000):
        a = i + 1
    print "finished counting..."

'''
running count() method in a subsquential order
'''
start_time = datetime.datetime.now()
print "running count() twice"
count()
count()
end_time = datetime.datetime.now()
 
print end_time - start_time
 
'''
running count() method in a native threading manner
'''
class CountThread(threading.Thread):
    def run(self):
        count()
 
print "running count() as two threads"
c1 = CountThread()
c2 = CountThread()
start_time = datetime.datetime.now()
c1.start()
c2.start()
c1.join()
c2.join()
end_time = datetime.datetime.now()
print end_time - start_time

'''
running count() in a green threading manner
'''
print "running count() as two green threads"

start_time = datetime.datetime.now()

pool = GreenPool()
pool.spawn(count())
pool.spawn(count())

end_time = datetime.datetime.now()
print end_time - start_time