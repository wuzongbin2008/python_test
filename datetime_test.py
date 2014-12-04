import datetime
import time


now = datetime.datetime.now()
#print "time.time() = %s" % time.time()

#print now.second
time_str = time.localtime(1415908827)
print "time_str = %s" % time_str
yesterday = time.strftime('%Y-%m-%d', time_str)
#print "yesterday = %s" % yesterday

#print "Y = %s" % time.strftime('%Y', time_str)