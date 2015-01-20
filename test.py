import commands, os, re  
import json
import sys


def get_name():
    print sys._getframe()
    print sys._getframe().f_code
    print sys._getframe().f_code.co_name

def scope_test():
    try:
        for i in 1:
            if i == 4:
                a = "a4"
            else:
                a = "b"
        print a
    except Exception,e:
        print "ex"
        raise

    print a

if __name__ == "__main__":
    try:

        a = 0
        b = 1
        c = 2
        d = 0
        print c & 1
    except Exception,e:
        print "main: %s" % e.args
