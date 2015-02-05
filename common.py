import os
import sys
import time
import re
import urllib2
import httplib2
import commands
import threading
import storageservice as ss

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

def worker():
    i = 10
    for i in range(5):
        time.sleep(1)
        print "worker_1 : %s\n" % i
        i += 1
    return

def worker2():
    i = 0
    for i in range(5):
        print "worker_2 : %s\n" % i
        i += 1
    return

def demo_thread():
    t = threading.Thread(target=worker)
    #t.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t2.start()
    t.start()
    #t.join()

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

def read_test(file):
    fp = open(file,"r")
    return fp.readlines()

def write_test(path):
    fp = open(path,"a")
    fp.write("%s" % "test\n")
    fp.flush()

def replace():
    dir = "/opt/portraits/000/004"
    print dir.lstrip("/").replace("/","_")

def urllib2_down_file(url,line):
    buffer = None
    #print "url = %s" % url
    u = urllib2.urlopen(url)
    meta = u.info()
    file_size_ori = int(meta.getheaders("Content-Length")[0])

    file_size_dl = 0
    block_sz = 8192
    while file_size_dl < file_size_ori:
        buffer = u.read(block_sz)
        #print "buffer = %s" % buffer
        if len(buffer) == 0:
            print "buffer_is_empty file_size_ori={file_size_ori} file_size_dl={file_size_dl} line={line}".format(file_size_ori=file_size_ori,file_size_dl=file_size_dl,line=line)
            break

        file_size_dl += len(buffer)

    if file_size_ori != file_size_dl:
        print "size_is_not_equal file_size_ori={file_size_ori} file_size_dl={file_size_dl} line={line}".format(file_size_ori=file_size_ori,file_size_dl=file_size_dl,line=line)

    return buffer

def filer_test():
    line = "6795d6bf49b1fd2de739c /nfs_pics_filer28/n_pic/324/022/6795d6bf49b1fd2de739c.jpg 1"
    pid, path, flag = line.split(' ')
    print "pid=%s\npath=%s\nflag=%s" % (pid,path,flag)
    return pid

def get_url(pid, deleted=False) :
    ACCESS_KEY = '" "000000000" "IMG'
    SECRETE_KEY = 'UaOe3H3Rl4rITMCBJbPgDjWd6qZKQuWfIspfxzvq'
    PROJECT = 'storage." "img.cn'

    uid = "%d" % int(pid[0:8], 16)

    s3_path = os.path.join(uid, 'deleted', pid) if deleted \
            else os.path.join(uid, pid)

    #proxy = self.get_proxy()

    sh = ss.S3(ACCESS_KEY, SECRETE_KEY, PROJECT)
    sh.set_need_auth(True)
    #sh.set_proxy(proxy)
    return sh.get_file_url(s3_path)

def httplib2_down_file(url):
    h = httplib2.Http()
    #url = 'http://www.xxx.com/xxxx.zip'
    resp, content = h.request(url)
    return content

def create_logdir(self,path):
    if not os.path.exists(path):
        os.mkdir(path,0777)
        if not os.path.exists(path):
            print "create %s failed" % path
            sys.exit(1)

def regexp_test(text):
    pattern = ".*line=\((.*)\).*"
    s_ret = re.search(pattern,text)
    if s_ret:
        #print "match_0 : %s\n" % s_ret.group(0)
        print "key : %s\n" % s_ret.group(1)
        #print "filename : %s\n" % s_ret.group(2)

def process_info():
    pid = os.getpid()
    res = commands.getstatusoutput('ps aux|grep '+str(pid))[1].split('\n')[0]
    print res
    exit(0)
    p = re.compile(r'\s+')
    l = p.split(res)
    info = {'user':l[0],
        'pid':l[1],
        'cpu':l[2],
        'mem':l[3],
        'vsa':l[4],
        'rss':l[5],
        'start_time':l[6]}
    return info


if __name__ == "__main__":
    try:
        lines = read_test("./logs/ex.log")
        for line in lines:
            regexp_test(line)

    except Exception, e:
        print "e = %s" % e



