'''
Created on Jun 11, 2013

@author: shengjiemin
'''
from fabric.api import run


def hello():
    print("Hello World")

def host_type():
    run('uname -s')

#print("Executing on %(host)s as %(user)s" % env)


'''
user:
Fabric defaults to your local username when making SSH connections, but you can
use env.user to override this if necessary. The Execution model documentation
also has info on how to specify usernames on a per-host basis.

password:
Used to explicitly set your default connection or sudo password if desired.
Fabric will prompt you when necessary if this isn’t set or doesn’t appear to be
valid.
'''


'''
The settings context manager:
In many situations, it’s useful to only temporarily modify env vars so that a
given settings change only applies to a block of code. Fabric provides a
settings context manager, which takes any number of key/value pairs and will
use them to modify env within its wrapped block.
'''

'''
go is your new entry point (to be invoked as fab go, or whatnot) and its job is
to take the results dictionary from the execute call and do whatever you need
with it. 
'''