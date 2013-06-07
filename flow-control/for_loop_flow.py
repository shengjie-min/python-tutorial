'''
Created on May 26, 2013

@author: shengjiemin
'''


def for_loop_flow():
    for a in range(0, 2):
        print "a = %s" % a
#         flag = True
        for b in range(3, 5):
            print "b = %s" % b
            if b == 4:
                print "XXXXXXXXbreak"
                flag = False
                break
#         if flag == True:
        else: # for else gets rid of the flag here
            print "big piece of logic here, when it breaks, I don't wanna be here"

def for_loop_break():
    for a in range(0, 5):
        print a
        if a == 3:
            return
    print "big piece of logic here, when it breaks, I don't wanna be here"


for_loop_flow()
print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for_loop_break()
