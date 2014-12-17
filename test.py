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
        pid = "61ba5575gw6db0ngfeir9j"
        usid = "000G3CIojx06KDN0ZgFH010800pQMa0a01"
        fid = "003ecd43c0c17cea7217ce454364c0d10002a16b"
        print len(fid)
    except Exception,e:
        print "main: %s" % e.args
