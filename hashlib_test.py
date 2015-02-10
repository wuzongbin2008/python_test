import hashlib
import json
from common import debug

def read_test(file):
    fp = open(file,"r")
    return fp.read()

def md5_test():
    debug("md5_test")
    f2= "cc8acc06jw1eotnfkqq3vj20dc0dcq32.jpg"
    p = "./data/%s" % f2
    print "p: %s" % p
    c = read_test(p)
    #print len(c)
    dcs = hashlib.md5(c).hexdigest()
    print "dcs = %s" % dcs
    cs = "cdff6831f0acaf23b0be001a59de0229"
    print "cs = %s" % cs
    if dcs == cs:
        print "=="
    else:
        print "!="

def gen_fid_info():
    gfid_dict = {}
    sub_fidlist = ['ee2c4cefbd5c2ac045ffbcf73e3e1d82000252d8','64389e17c85a1717782de794443e1097000252d8']
    gfid_dict['version'] = 2
    gfid_dict['size'] = 1089
    gfid_dict['checksum'] =  "c406dd6d96ea6282e65a7fd7abf99399"
    gfid_dict['chunknum'] = 3
    gfid_dict['chunksize'] = 333
    gfid_dict['chunks'] = sub_fidlist
    gfid = json.dumps(gfid_dict)
    print gfid


if __name__ == "__main__":
    try:
        md5_test()

    except Exception, e:
        print "e = %s" % e