'''
Created on May 27, 2013

@author: shengjiemin
'''
from __future__ import absolute_import
from celery import Celery

'''
The first thing you need is a Celery instance, this is called the celery
application or just app in short.

The first argument to Celery is the name of the current module,
this is needed so that names can be automatically generated,
the second argument is the broker keyword argument which specifies the URL of
the message broker you want to use, using RabbitMQ here, which is already the
default option. See Choosing a Broker above for more choices, e.g. for Redis
you can use redis://localhost, or MongoDB: mongodb://localhost.
'''
celery = Celery('proj.celery_worker_server',
                # if you want to use Redis as the result backend, but still
                # use RabbitMQ as the message broker (a popular combination)
                #backend='redis://localhost'
                broker='amqp://guest:guest@localhost:5672//',
                include=['celery_tasks'])

if __name__ == '__main__':
    ''' 
    Commands:

    1. python celery_worker_server.py worker -l info
        to start worker server
    2. python celery_work_server.py worker -B -l info
        to start both worker and beat
    3. python celery_work_server.py beat -l info
        only starts beat
    4. python celery_work_server.py beat -l info -P eventlet -c 1000
        use eventlet as the backend execution pool with 1000 concurrency

        By default multiprocessing is used to perform concurrent execution
        of tasks, but you can also use Eventlet.
    '''
    celery.start()
