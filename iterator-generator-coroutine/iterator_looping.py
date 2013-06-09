'''
Created on May 12, 2013

@author: shengjiemin
'''


def my_dictionary():
    my_dict = dict(aaa = 1, bbb = 2)
    print my_dict
    my_iter = my_dict.iteritems();
    print my_iter
    for k, v in my_dict.iteritems():
        if k.startswith("a"):
            print k, v

my_dictionary()
