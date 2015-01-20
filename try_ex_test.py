__author__ = 'wj'


def raise_t():
    try:
        n = 0
        print "start raise"
        raise Exception("raise_t failed")
        print "end raise"
    except Exception,e:
        raise Exception("raise exception reason: %s" % e)

if __name__ == "__main__":
    try:
        n = 0
        a = 10/n
    except Exception,e:
        print "main exception: %s" % e

    print "end"