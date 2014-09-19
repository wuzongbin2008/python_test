#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

start = 0 #int(sys.argv[1])
stop = 10 #int(sys.argv[2])
sizes = [180,50,30]

basedir = "/opt/portraits"

list = map(lambda x:"%03d" % x,range(0,10))

def create_file(dir,file,i,j):
    fp = open(file,"w")
    fp.write("%s/f_%s_%s" % (dir2,i,j))
    fp.flush()

for i in list[start:stop+1]:

    uid = "3271972257"
    uid2 = "1378181244"

    try:

        dir1 = "%s/%s" % (basedir, i)
        print "dir1 = %s" % dir1
        os.mkdir(dir1, 755)

    except Exception,e:
        print e

    for j in list:
        try:
            dir2 = "%s/%s/%s" % (basedir, i, j)
            print "dir2 = %s" % dir2
            os.mkdir(dir2, 755)

            for size in sizes:
                file = "%s/%s.01.%s" % (dir2,uid,size)
                print file
                create_file(dir2,file,i,j)
                file2 = "%s/%s.01.%s" % (dir2,uid2,size)
                print file2
                create_file(dir2,file2,i,j)

        except Exception,e:
            print e

