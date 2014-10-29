import hashlib
import json

def read_test(file):
    fp = open(file,"r")
    return fp.read()

def md5_test():
    c = read_test("./1.jpg")
    print len(c)
    print hashlib.md5(c).hexdigest()

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
        gen_fid_info()

    except Exception, e:
        print "e = %s" % e