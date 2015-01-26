import os
import sys
import time
import re
import gio
import urllib2
import httplib2
import commands
import threading

sys.path.append('./lib')

i = 0
j = 0

def read_dir():
    if len(sys.argv) == 1:
        root = "/weibo_img/"
    else:
        root = sys.argv[1]

    i = 0
    k = 0
    for dir_name, sub_dirs, files in os.walk(root,True):
        i += 1
        #sub_dirs = ["%s/" % n for n in sub_dirs]
        contents = files
        contents.sort()
        print sub_dirs
        #print dir_name
        #print files
        break

    if "data5" in sub_dirs:print "exsit"

    if sub_dirs.count("data5"):print "exsit2"
    # for filename in contents:
    #     k += 1
    #     print "%s\t" % filename
    # print "\n"
    # print k

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

def get_files_bypath():
    path = "/opt/portraits/009/"
    try:
        subs = list(os.walk(path, topdown=False))
        dir_files = []
        #print subs
        while len(subs):
            d = subs.pop()
            if len(d[2]) > 0:
                dir_files.append(d)
        print "dir_total: %d" % len(dir_files)
        for d in dir_files:
            print d
    except Exception,e:
        print "get_files_bypath path='{pa}' exception out='{out}'".format(pa=path, out=repr(e))

def test_ex():
    try:
        sys.exit("a")
    except SystemExit, e:
        print e.message

def readlines_test(file):
    fp = open(file,"r")
    return fp.readlines()

def read_test():
    file = "./data/identifier"
    fp = open(file,"r")
    i = 0
    for line in fp:
        i+=1

        if line.count("city"):
            arr = line.split(":")
            print "%d: %s" %(i,line)
    return fp.read()

def write_test():
    try:
        d = 0
        path = "./data/a_plus.txt"
        content = "file write test5"
        fp = open(path,"w+")
        fp.write("%s" % str(content))

        r = 10/0
        #fp.flush()
    except Exception,e:
        print e

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
    file = "./data/2946117692.01.180"
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

def parse_host_ip():
    f = "./data/host_ip"
    fp = open(f,"r")
    for l in fp:
        host_ip = l.strip().split(" ")
        if len(host_ip) == 2:
            print host_ip

def check_path_available():
    path = "b.txt"
    ret= os.access(path, os.F_OK|os.W_OK|os.R_OK|os.X_OK)
    print "ret: %s"%ret
    if ret :
        print "b.txt is ok"
    else:
        print "b.txt is unavailable"


if __name__ == "__main__":
    try:

        get_file_mime()

    except Exception, e:
        print "e = %s" % e



