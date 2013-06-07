'''
Created on May 26, 2013

@author: shengjiemin
'''


urls = ["http://www.google.com/intl/en_ALL/images/logo.gif",
     "http://s1.djyimg.com/i6/911251851061487.jpg",
     "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif"]

import eventlet
from eventlet.green import urllib2

def fetch(url):
    print "opening", url
    body = urllib2.urlopen(url).read()
    print "done with", url
    return url, body


pool = eventlet.GreenPool(200)
for url, body in pool.imap(fetch, urls):
    print "got body from", url, "of length", len(body)