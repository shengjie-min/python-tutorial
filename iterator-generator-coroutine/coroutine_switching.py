'''
Created on Jun 9, 2013

@author: shengjiemin

A coroutine is a function that can be suspended and resumed, and can have
multiple entry points

Cooperative multitasking and asynchronous I/O using generators

multitask implements coroutines, task added must be a generator, when it yields,
multitask switchs to next task
'''
import multitask
import time
 
def coroutine_1():
    for i in range(3):
        print 'c1'
        yield i
 
def coroutine_2():
    for i in range(3):
        print 'c2'
        # uncomment this line to get it working
        # otherwise
        # TypeError: 'task' must be a generator

        # yield i
 
def coroutine_3():
    for i in range(3):
        print 'c3'
        yield i
 
multitask.add(coroutine_1())
multitask.add(coroutine_2())
multitask.add(coroutine_3())
 
multitask.run()
