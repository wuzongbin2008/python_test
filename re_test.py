import re
from common import read_test


def regexp_test(text):
    pattern = ".*line=\((.*)\).*"
    pattern = ".*-recover_check_failed_pid"
    s_ret = re.search(pattern,text)
    if s_ret:
        #print "match_0 : %s\n" % s_ret.group(0)
        print "key : %s\n" % s_ret.group(0)
        #print "filename : %s\n" % s_ret.group(2)



if __name__ == "__main__":
    try:
        str="/usr/home/wujiang1/imgbed_tools/recover_not_upload_idc/pid_lost_log_2014-10-09-recover_check_failed_pid"
        regexp_test(str)

    except Exception, e:
        print "e = %s" % e