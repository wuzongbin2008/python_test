import datetime
import time

SECONDS_PER_DAY = 0#24*3600

def get_yesterday() :
    time_str = time.localtime(time.time() - SECONDS_PER_DAY)
    yesterday = time.strftime('%Y-%m-%d', time_str)
    return yesterday

now = datetime.datetime.now()
print "now = %s" % time.time()

#print now.second
time_str = time.localtime(1415908827)
print "get_yesterday() = %s" % get_yesterday()
yesterday = time.strftime('%Y-%m-%d', time_str)
#print "yesterday = %s" % yesterday

#print "Y = %s" % time.strftime('%Y', time_str)