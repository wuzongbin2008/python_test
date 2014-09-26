import os
import sys


def split_t(str):
    str = "/weibo_img/data7"
    DEV_INDEX = 2
    DEV_LEN = 3
    disc = str.split('/')[DEV_INDEX][0:DEV_LEN]
    print str.split('/')
    print disc

def eval_test(str):
    left_bound  = str.find('{')
    right_bound = str.rfind('}') + 1
    info = eval(str[left_bound:right_bound])
    for k in info:
        print "%s = %s" % (k,info[k])


if __name__ == "__main__":
    str = "2014-01-20 23:59:50,462 - checkin - INFO - (16467)process msg succ: {u'ip': u'10.75.24.41', 'store_id': 'data208'" \
          ", u'exif': {u'YResolution': 72, u'ResolutionUnit': u'inches', u'CustomRendered': u'Normal', u'ColorSpace': u'sRGB'" \
          ", u'ExifImageWidth': 500, u'YCbCrPositioning': u'centered', u'XResolution': 72, u'WhiteBalance': u'Manual', " \
          "u'ExifImageLength': 335}, u'checksum': u'45ecb23cc03368600a2d81cad22921c1', u'app': u'428430', u'pid': " \
          "u'abe74fb0jw1ecqg9ehtl0j20dw09bt9z', u'ext': u'.jpg', 'fid': u'45ecb23cc03368600a2d81cad22921c10000df7b', u'timestamp': " \
          "1390233590, u'cs': {u'large': u'45ecb23cc03368600a2d81cad22921c1', u'mw690': u'454e60c2af8f32dbb704a7442ea17676', " \
          "u'thumbnail': u'ae2e4298ea6ccc689e7a290e8ed7de08', u'bmiddle': u'51e474378090809515b01c3bceab54c7'}, 'pic_path': " \
          "'/069/236/', u'size': 57211} - filer_path: /weibo_img/filer_cache/t_cache/022/183/abe74fb0jw1ecqg9ehtl0j20dw09bt9z - " \
          "NOTFS, elapse: 0.068"

    eval_test(str)