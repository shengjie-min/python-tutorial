'''
Created on May 12, 2013

@author: shengjiemin
'''
import json


def my_json_dump():
    my_dict = {'aaa': 1, 'bbb': 2}
    print my_dict
    my_dict_dump = json.dumps(my_dict)
    print my_dict_dump
    json.loads(my_dict)

my_json_dump()