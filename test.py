import commands, os, re  
import json

str = '{"version":1,"callbacks":1,"param":{"uid":222,"pid":333,"count":1,"size":100,"height":55,"length":66,"format":1,"exif":".jpg","ip":"127.0.0.1","appid":5}}'

a=json.loads(str)

try:
    f = False
    if f:print 1
except Exception,e:
    print e.args
