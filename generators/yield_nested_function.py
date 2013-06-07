'''
Created on May 16, 2013

@author: shengjiemin
'''

def outter():
    def inner():
        for i in range(0,4):
            print "yield " + str(i)
            yield i
            
    gen = inner()
    for k in gen:
        print k
animals = []
def my_generator(my_case=False):
    if my_case:
        for a in animals:
            yield mymodels.Animal(
                                name=a['name'],
                                type=a['type'],
                                height=a['height'],
                                country=a['country']
                        )
    else:
        for a in animals:
            # some logic Check
            # real case is more complex, this condition is just making a point here
            if a['name'] != 'jack':
                yield mymodels.Animal(
                        name=a['name'],
                        type=a['type'],
                        height=a['height'],
                        country=a['country']
                        )