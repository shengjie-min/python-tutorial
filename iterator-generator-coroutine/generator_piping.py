'''
Created on Mar 18, 2013

@author: shengjiemin
'''


def fibonacci():
    a, b  = 0, 1
    while True:
        yield b
        a, b = b, a + b


def power(values):
    for value in values:
        print 'powering %s' % value
        yield value


def adding(values):
    for value in values:
        print 'adding %s' % value
        yield value

fib = fibonacci()
print fib
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()

elements = [1, 2, 3, 4, 5]
pwr = power(elements)
add = adding(pwr)
print pwr

print add
add.next()
add.next()
add.next()
add.next()
add.next()
print "sequence gets exhuasted here"
add.next()

