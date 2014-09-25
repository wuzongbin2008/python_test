import datetime
import time


now = datetime.datetime.now()

#print now.second
time_str = time.localtime(time.time() - 24*3600)
print time_str
yesterday = time.strftime('%Y-%m-%d', time_str)
print yesterday