import re
from file_test import read_test
from file_test import readlines_test

def regexp_test():
    str="/usr/home/wujiang1/imgbed_tools/recover_not_upload_idc/pid_lost_log_2014-10-09-recover_check_failed_pid"

    text2 = '2014-10-28 18:35:28,895 - replicate.BJ - INFO - (23272)process msg succ: {"ip": "221.205.70.6", "exif": {"YResolution": 72, "ResolutionUnit": "inches", "CustomRendered": "Normal", "ColorSpace": "sRGB", "ExifImageWidth": 848, "YCbCrPositioning": "centered", "XResolution": 72, "WhiteBalance": "Manual", "ExifImageLength": 480}, "checksum": "52b970e956475d524693cb123b59d06b", "app": 28, "pid": "005JDhf9jw1elr20i7xsyj30nk0dcta0", "ext": ".jpg", "timestamp": 1414492529, "cs": {"large": "52b970e956475d524693cb123b59d06b", "mw690": "c4d332a896f0ea14a60068ba2e64c739", "thumbnail": "a121348e4aad977292485d3f3db204dc", "bmiddle": "8af5a4ab76348bda4ebf605e4c10b6d4"}, "size": 58198}, elapse: 0.16 2014-10-28 18:35:28,903 - replicate.BJ - INFO - (23248)process msg succ: {"ip": "10.73.14.212", "exif": {"ExifImageWidth": 720, "ExifImageLength": 720}, "checksum": "fd427a36a4077919e56db49524d9c9cf", "app": 333536, "pid": "005PWtcijw8elr20i7511j30k00k0mxz", "ext": ".jpg", "timestamp": 1414492529, "cs": {"large": "fd427a36a4077919e56db49524d9c9cf", "mw690": "1090698676d677e5566f5e0ed34f8f11", "thumbnail": "023acab99f493a61c5836ef2d008b872", "bmiddle": "d9948d4a9f81e54ab1a26692e5945b9f"}, "size": 40621}, elapse: 0.217'
    text1 = '2014-10-28 18:26:54,478 - replicate.BJ - ERROR - (23222)set mq back succeeded, reason: \'cs\', msg: {"size": 900, "uid": 1414033353, "timestamp": 1414141747, "ip": "", "chunk": {"count": 1, "info": [{"size": 900, "md5": "7d0d0e8ea55e0627823181becac3030e"}], "chunk_size": 20971520}, "rep_retry": 5652320, "pid": "001xH8Fzjx06N28PlQwD040f010000ew0k01", "project": "wbcamer", "version": 2, "appid": 0, "checksum": "7d0d0e8ea55e0627823181becac3030e", "type": "", "proid": 4}'

    text1 = "data162.bj.storage.t." "img.cn"
    pattern = ".*line=\((.*)\).*"
    pattern = ".*-recover_check_failed_pid"

    pattern = ".*\"(chunk\":\s+\{\"count\":\s+\d+,\s+\"info\":\s+\[.*],\s+\"chunk_size\":\s+\d+\}).*\"rep_retry\":\s+(\d+).*\"pid\": \"([A-Za-z0-9]+)\","
    pattern = "(data\d+)\.bj.+"
    pattern = ".*_data=(.+)\s+(.*)\s+Profile:\s*\[.*\:([\d\.]*)\]{1}\s+\[{1}.*\:([\d\.]*)\]\s+\[.*\:([\d\.]*)\]\s+\[.*\:([\d\.]*)\]"

    text1="accesskey=picserversweibof6vwt&_ip=10.75.60.118&_port=80&_an=IBM13060013&_data=2014-11-10 13:02:31 Profile: [resize-bmiddle:0.0084] [resize-thumbnail:0.0048] [resize-mw690:0.009] [publish:0.003]"

    text1 = "111 http://www.baidu.com/aaa"
    pattern = ".*\s+(http://.*)"
    s_ret = re.search(pattern,text1)
    if s_ret:
        #print s_ret.group(0)
        print s_ret.group(1)
        # print s_ret.group(2)
        # print s_ret.group(3)
        # print s_ret.group(4)
        # print s_ret.group(5)
        # print s_ret.group(6)
    else:
        print "no match"

def parse_rep_retry_log():
    err_log = "./log/replicate.log.BJ.2014-10-24"
    fp = open(err_log,"r")

    pattern = ".*\"rep_retry\":\s+(\d+).*\"pid\": \"([A-Za-z0-9]+)\","

    n = 0
    pids = []

    for line in fp:
        print line
        #exit(0)
        n += 1
        s_ret = re.search(pattern,line)
        if s_ret:

            #print "line %d: %s\n" % (n,s_ret.group(0))
            retry_cnt =  int(s_ret.group(1))
            pid = s_ret.group(2)
            if retry_cnt > 10:
                #print "%d retry_cnt = %d\npid = %s\npid_len = %d" % (n,retry_cnt,pid,len(pid))
                #print "%d pid = %s" % (n,pid)
                if pids.count(pid) == 0:
                    pids.append(pid)
        else:
            print "no match %d: %s" % (n,line)
        #exit(0)
    print pids

def data_corrupted():
    er_msg = '2015-02-09 09:38:54,111 - replicate.BJ - ERROR - (2964)set mq back succeeded, reason: data corrupted: [50e7f9ba23d8931bfa162b82e4fd1595] [da6d339a0e4d43bd14980896c27787fe], msg: {"exif": {"YResolution": 72, "ResolutionUnit": "inches", "CustomRendered": "Normal", "ColorSpace": "sRGB", "ExifImageWidth": 150, "YCbCrPositioning": "centered", "XResolution": 72, "WhiteBalance": "Manual", "ExifImageLength": 150}, "ip": "10.75.5.93", "app": "862832", "rep_retry": 1300559, "pid": "c63dc28ejw1ep10mxqejqj2046046jr7", "ext": ".jpg", "timestamp": 1423308269, "cs": {"large": "50e7f9ba23d8931bfa162b82e4fd1595", "mw690": "88e7122368d33d2bc6f85a0b7992dfd4", "thumbnail": "e931dd8341be28b946ae21767352facc", "bmiddle": "50e7f9ba23d8931bfa162b82e4fd1595"}, "checksum": "50e7f9ba23d8931bfa162b82e4fd1595", "size": 3642}'

    pattern = "data\s+corrupted:"
    s_ret = re.search(pattern, er_msg)
    if s_ret:
        print "match"
    else:
        print "no match"


if __name__ == "__main__":
    try:

        data_corrupted()

    except Exception, e:
        print "e = %s" % e