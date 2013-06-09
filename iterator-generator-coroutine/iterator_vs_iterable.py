'''
Created on Jun 10, 2013

@author: shengjiemin


Iteration is a general term for taking each item of something, one after
another. Any time you use a loop, explicit or implicit, to go over a group of
items, that is iteration.

In Python, iterable and iterator have specific meanings.

An iterable is an object that has an __iter__ method which returns an iterator,
or which defines a __getitem__ method that can take sequential indexes starting
from zero (and raises an IndexError when the indexes are no longer valid). So
an iterable is an object that you can get an iterator from.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

When every you use a for loop, or map, or a list comprehension, etc. in Python,
the next method is being called automatically to get each item from the
iterator, thus going through the process of iteration.
'''


class Roster(object):

    def __init__(self, *arg):
        self.entries = arg
        self.index = 0
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.index >= len(self.entries):
            raise StopIteration
        else:
            name = self.entries[self.index]
            self.index += 1
            return name

    def seek(self, n):
        self.index=n

roster = Roster("shengjie", "yuxia")

for r in roster:
    print r

roster.seek(0)
print roster.next()
print roster.next()
roster.next()