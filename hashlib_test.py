import hashlib

def read_test(file):
    fp = open(file,"r")
    return fp.read()


if __name__ == "__main__":
    try:
        c = read_test("./1.jpg")
        print len(c)
        print hashlib.md5(c).hexdigest()

        #de150cd748352aa393efe2a4abe818ef
        #de150cd748352aa393efe2a4abe818ef
        #90383fec4ab82eb62f62c87c02174e0b

    except Exception, e:
        print "e = %s" % e