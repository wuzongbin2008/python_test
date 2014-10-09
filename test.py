import commands, os, re  
import json

str = '{"version":1,"callbacks":1,"param":{"uid":222,"pid":333,"count":1,"size":100,"height":55,"length":66,"format":1,"exif":".jpg","ip":"127.0.0.1","appid":5}}'

a=json.loads(str)

try:
    local_idc = "TJ"
    list = ['BJ', 'TJ', 'GZ']
    if local_idc not in  list:

        print local_idc

    else:
        print "test"
        list[i]
        exit(1)
        print local_idc
except Exception,e:
    print e.args
