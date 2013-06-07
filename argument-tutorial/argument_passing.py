'''
Created on May 21, 2013

@author: shengjiemin
'''


def argument_passing(must_field):
    print must_field


def argument_no_passing(optional_field=None):
    print optional_field


# this is going to succeed because optional_field has a default value
argument_no_passing()

# this is going to fail because must_field is mandatory
argument_passing()