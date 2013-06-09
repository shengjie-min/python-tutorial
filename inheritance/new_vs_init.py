'''
Created on Jun 10, 2013

@author: shengjiemin


__new__ is the first step of instance creation. It's called first, and is
responsible for returning a new instance of your class. In contrast, __init__
doesn't return anything; it's only responsible for initializing the instance
after it's been created.
'''

class Agent(object):
    _agents = dict()

    def __new__(cls, *p):
        number = p[0]
        if not number in cls._agents:
            cls._agents[number] = object.__new__(cls)
        return cls._agents[number]

    def __init__(self, number):
        self.number = number

    def __eq__(self, rhs):
        return self.number == rhs.number

if Agent("a") is Agent("a"):
    print Agent("a")
    print "YES"

