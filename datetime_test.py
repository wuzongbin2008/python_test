import datetime
import time

SECONDS_PER_DAY = 0#24*3600

def get_yesterday() :
    ms = time.time()
    microsecond = (ms - long(ms)) * 1000
    time_str = time.localtime(time.time() - SECONDS_PER_DAY)
    dt = time.strftime('%Y-%m-%d %H:%M:%S', time_str)
    s = "%s,%03d" % (dt, microsecond)
    print s

def get_micros() :
    ms = time.time()
    print ms
    print long(ms)
    microsecond = (ms - long(ms)) * 1000
    print microsecond


get_micros()