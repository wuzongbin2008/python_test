import os
import re
import commands

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

print 1%256
# files = os.listdir("/home/wj/")
# for f in files:
#     print f