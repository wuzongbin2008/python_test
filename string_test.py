import os
import sys

UNISTORE_PROJECTS = {
	0 :   {
		"name" : 'sandbox',
		"max_size" :500000,
		"skey" : "11111111"
	},
	1 :   {
		"name" : 'video',
		"max_size" : 2000000000,
		"skey" : "os[n@cW8b8oKHpJJh%s_|9Ux5MN`AXK8"
	},
	2 :   {
		"name" : 'tuding',
		"max_size" : 3000000000,
		"skey" : "L:c|k/\yHo>pbW]E=qchLc^}`g$]z//B"
	},
	3 :   {
		"name" : 'miaopai',
		"max_size" :  500000000,
		"skey"	: "/n9WQl@=396]K/<=5LTRzF@g9[:+T]_&"
	},
	4 :   {
		"name" : 'wbcamer',
		"max_size" : 500000000,
		"skey" :"Om@Id$Quav{og(iAc>vi=ov+wuCs;E)O"
	},
}

def split_t():
    str = "/data0/daemons/lost_pic_count/logs/pid_lost_log_2014-10-08"
    str = "/usr/home/wujiang1/imgbed_tools/recover_not_upload_idc/pid_lost_log_2014-10-09-recover_check_failed_pid"
    DEV_INDEX = 2
    DEV_LEN = 3
    disc = str.split('/')
    print disc
    print len(disc)
    print disc.pop()

def eval_test():
    str = "2014-01-20 23:59:50,462 - checkin - INFO - (16467)process msg succ: {u'ip': u'10.75.24.41', 'store_id': 'data208'" \
          ", u'exif': {u'YResolution': 72, u'ResolutionUnit': u'inches', u'CustomRendered': u'Normal', u'ColorSpace': u'sRGB'" \
          ", u'ExifImageWidth': 500, u'YCbCrPositioning': u'centered', u'XResolution': 72, u'WhiteBalance': u'Manual', " \
          "u'ExifImageLength': 335}, u'checksum': u'45ecb23cc03368600a2d81cad22921c1', u'app': u'428430', u'pid': " \
          "u'abe74fb0jw1ecqg9ehtl0j20dw09bt9z', u'ext': u'.jpg', 'fid': u'45ecb23cc03368600a2d81cad22921c10000df7b', u'timestamp': " \
          "1390233590, u'cs': {u'large': u'45ecb23cc03368600a2d81cad22921c1', u'mw690': u'454e60c2af8f32dbb704a7442ea17676', " \
          "u'thumbnail': u'ae2e4298ea6ccc689e7a290e8ed7de08', u'bmiddle': u'51e474378090809515b01c3bceab54c7'}, 'pic_path': " \
          "'/069/236/', u'size': 57211} - filer_path: /weibo_img/filer_cache/t_cache/022/183/abe74fb0jw1ecqg9ehtl0j20dw09bt9z - " \
          "NOTFS, elapse: 0.068"
    left_bound  = str.find('{')
    right_bound = str.rfind('}') + 1
    info = eval(str[left_bound:right_bound])
    for k in info:
        print "%s = %s" % (k,info[k])

def join_test():
    s1="a"
    print s1
    s1+="b"
    print s1
    s1 +="c"
    print s1

def parse_fid():
    fid = 'ee2c4cefbd5c2ac045ffbcf73e3e1d82000252d8'
    md5 = fid[0:32]
    size = int(fid[32:40],16)
    return md5,size

def get_project_no(pro_name):
    pro_no = None
    for pro_no in UNISTORE_PROJECTS:
        if UNISTORE_PROJECTS[pro_no]['name'] == pro_name.strip():
            return pro_no
    return pro_no

if __name__ == "__main__":

    md5,size = parse_fid()
    print md5
    print size
