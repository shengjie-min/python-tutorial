'''
Created on Jun 10, 2013

@author: shengjiemin
'''
from celery.schedules import crontab
from celery.task import periodic_task
from celery_worker_server import celery

'''
defined a single task, called period_task, which runs every min
'''
@periodic_task(run_every=crontab())
def period_task():
    print "this is a priodic task running every min"

'''
defined a single task, called add, which returns the sum of two numbers
'''
@celery.task
def add(x, y):
    return x + y