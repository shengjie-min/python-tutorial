'''
Created on Jun 10, 2013

@author: shengjiemin
'''
from celery_tasks import add
'''
To call our task you can use the delay() method.

This is a handy shortcut to the apply_async() method which gives greater
control of the task execution
'''

add.delay(4, 4)
add.delay(5, 5)
add.delay(6, 6)
add.delay(7, 7)