'''
Created on May 24, 2013

@author: shengjiemin
'''
def if_empty_list_flow():
    if []:
        print "empty [] is true"
    else:
        print "empty [] is false"


def if_empty_string_flow():
    if "":
        print "empty string is true"
    else:
        print "empty string is false"


def if_empty_dict_flow():
    if {}:
        print "empty dict is true"
    else:
        print "empty dict is false"


def if_none_flow():
    if None:
        print "None is true"
    else:
        print "None is false"


if_empty_list_flow()
if_empty_string_flow()
if_empty_dict_flow()
if_none_flow()

