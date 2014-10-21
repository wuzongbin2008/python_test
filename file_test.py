import os
import sys
import time
import re
import gio
import urllib2
import httplib2
import commands
import threading
#import sinastorageservice as ss

i = 0
j = 0

def read_dir():
    if len(sys.argv) == 1:
        root = "/opt/portraits"
    else:
        root = sys.argv[1]

    i = 0
    k = 0
    for dir_name, sub_dirs, files in os.walk(root):
        i += 1
        sub_dirs = ["%s/" % n for n in sub_dirs]
        contents = files
        contents.sort()
        print dir_name

    for filename in contents:
        k += 1
        print "%s\t" % filename
    print "\n"
    print k

def get_allfiles():
    search_dir = "/opt/portraits"
    ispic = False
    #try:
    lists = os.walk(search_dir).next()[1]
    print "lists len = %d\n" % len(lists)
    print lists
    if len(lists) == 0:
        sys.exit(0)

    lists.sort()
    src_dir, tmp, files = os.walk(search_dir + lists[0]).next()
    filelist = []
    for file in files:
        print file
        # except SystemExit,e:
        #     raise e.SystemExit(0)
        # except Exception,e:
        #     msg = "Panic: get_allfiles: %s" % e.message
        #     #print msg
        #     raise Exception, msg

def test_ex():
    try:
        sys.exit("a")
    except SystemExit, e:
        print e.message

def readlines_test(file):
    fp = open(file,"r")
    return fp.readlines()

def read_test(file):
    fp = open(file,"r")
    return fp.read()

def write_test(path):
    fp = open(path,"a")
    fp.write("%s" % "test\n")
    fp.flush()

def replace():
    dir = "/opt/portraits/000/004"
    print dir.lstrip("/").replace("/","_")

def filer_test():
    line = "6795d6bf49b1fd2de739c /nfs_pics_filer28/n_pic/324/022/6795d6bf49b1fd2de739c.jpg 1"
    pid, path, flag = line.split(' ')
    print "pid=%s\npath=%s\nflag=%s" % (pid,path,flag)
    return pid

def create_logdir(self,path):
    if not os.path.exists(path):
        os.mkdir(path,0777)
        if not os.path.exists(path):
            print "create %s failed" % path
            sys.exit(1)

def pwd():
    print os.getcwd()

def get_file_mime():
    file = "./1.jpg"
    gio_file = gio.File(file)

    # gio_file_info = gio_file.query_info(",".join([
    # gio.FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE,
    # gio.FILE_ATTRIBUTE_STANDARD_TYPE,
    # gio.FILE_ATTRIBUTE_STANDARD_NAME,
    # gio.FILE_ATTRIBUTE_STANDARD_DISPLAY_NAME,
    # gio.FILE_ATTRIBUTE_STANDARD_SIZE,
    # gio.FILE_ATTRIBUTE_STANDARD_ICON,
    # gio.FILE_ATTRIBUTE_TIME_MODIFIED,
    # gio.FILE_ATTRIBUTE_TIME_CHANGED,]))

    gio_file_info = gio_file.query_info(",".join([
    gio.FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE,]))

    info_attr = gio_file_info.get_attribute_as_string(gio.FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE)

    type_description = gio.content_type_get_description(info_attr)
    #print type_description

    mime_tye = gio.content_type_get_mime_type(info_attr)
    print mime_tye


if __name__ == "__main__":
    try:
        get_file_mime()

    except Exception, e:
        print "e = %s" % e



