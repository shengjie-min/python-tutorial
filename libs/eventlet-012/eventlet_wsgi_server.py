'''
Created on Jun 9, 2013

@author: shengjiemin
'''
from eventlet import wsgi
import eventlet

def handler(env, start_response):
    for i in range(10000000):
        a = i
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']

wsgi.server(eventlet.listen(('localhost', 50010)), handler)