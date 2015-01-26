__author__ = 'wj'


def raise_t():
    try:
        n = 0
        print "before raise"
        raise Exception("raise_t failed")
        print "after raise"
    except Exception,e:
        raise Exception("raise exception reason: %s" % e)

if __name__ == "__main__":
    try:
        n = 0
        raise_t()
    except Exception,e:
        print "main exception: %s" % e

    print "end"