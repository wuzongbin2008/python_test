__author__ = 'wj'

class DataCorruptedException(Exception):
    pass

def finally_test():
    try:
        flag = 1
        val = ""
        if flag:
            val = 1
        else:
            print 'fuck'
        return val
    except Exception,e:
        print "e: %s" % e
    finally:
        print "finally_test finally"

def get_file_mime(file):
    #mime_type = ""
    fp = open(file,"r")
    str = fp.read(4)

    if len(str) >= 4:
        if ord(str[0]) == 0xff and ord(str[1]) == 0xd8:
            mime_type = "image/jpeg"

        elif ord(str[0]) == 0x89 and str[1:] == "PNG":
            mime_type = "image/png"

        elif str[0:3] == "GIF":
            mime_type = "image/gif"

        elif str[0:] == "RIFF":
            mime_type = "image/webp"
        else:
            mime_type = "text/plain"
    #print "mime_type: %s" % mime_type
    return mime_type

def get_str():
    if True:
        mine_type = "abc"
    return mine_type

def raise_t():
    try:
        n = 0
        print "before raise"
        raise DataCorruptedException("raise_t failed")
        print "after raise"
    except DataCorruptedException,e:
        raise DataCorruptedException("raise_t DataCorruptedException")

    except Exception,e:
        raise Exception("raise_t Exception")

def referenced_before_assignment():
    try:
        mine_type = get_str()
        #print str
    except Exception, e:
        print "referenced_before_assignment ex: %s" % e

def exception_class_test():
    try:
        raise_t()
    except DataCorruptedException,e:
        print "exception_class_test DataCorruptedException: %s" % e
    except Exception,e:
        print "exception_class_test Exception"
        raise

if __name__ == "__main__":
    print "start\n"
    try:
        exception_class_test()

    except Exception,e:
        print "main exception: %s" % e

    print "\nend"