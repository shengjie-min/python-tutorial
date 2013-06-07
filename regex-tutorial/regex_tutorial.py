'''
Created on May 15, 2013

@author: shengjiemin
'''

import re
from test.test_iterlen import len


sample_filters = []
sample_filters.append("query 1")
sample_filters.append("query 2")

sample_filters = " AND ".join(sample_filters)

other_filters =  "query 3"

filters = sample_filters + " OR " + other_filters
print filters

filters = filters.split('OR')
or_results = []
for or_filter in filters:
    and_filter = or_filter.split("AND")
    and_results = []
    for f in and_filter:
        result = f + "\'s result"
        and_results.append(result)
    print "or the results here"
    print or_results.append(and_results)
print or_results
    
# for f in sample_filters:
#     g = re.search("(.*)\((.*),?\)", f)
#     fname = g.group(1).strip()
# 
#     fargs = [s.strip().replace('\'', '').replace('\"', '')
#                          for s in g.group(2).split(',')]
#     print "fname: "
#     print fname
#     print "fargs: "
#     print fargs

# A AND B
# A OR B
# (A AND B) OR C
# A AND (B OR C)