import re
from common import read_test


def regexp_test(text):
    pattern = ".*line=\((.*)\).*"
    s_ret = re.search(pattern,text)
    if s_ret:
        #print "match_0 : %s\n" % s_ret.group(0)
        print "key : %s\n" % s_ret.group(1)
        #print "filename : %s\n" % s_ret.group(2)



if __name__ == "__main__":
    try:
        lines = read_test("./logs/ex.log")
        for line in lines:
            regexp_test(line)

    except Exception, e:
        print "e = %s" % e