#!/usr/bin/env python
# encoding: utf-8
# vim:fileencoding=utf-8
"""
replicaion.py

Created by wucheng@staff.sina.com.cn on 2010-06-24.
Version 0.1
Copyright (c) 2010 Sina Corp. All rights reserved.
"""

import logging
import logging.handlers
import os.path
import os
import random_test
import time
import fcntl
import string
import re

class NewLogHandler( logging.handlers.TimedRotatingFileHandler ):
    """
    Fix the bug that stat checking after existence checking of log file
    raises an OSError
    r"""
    
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=0, utc=0):
        logging.handlers.TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc)
        self.when = string.upper(when)
        self.backupCount = backupCount
        self.utc = utc
        # Calculate the real rollover interval, which is just the number of
        # seconds between rollovers.  Also set the filename suffix used when
        # a rollover occurs.  Current 'when' events supported:
        # S - Seconds
        # M - Minutes
        # H - Hours
        # D - Days
        # midnight - roll over at midnight
        # W{0-6} - roll over on a certain day; 0 - Monday
        #
        # Case of the 'when' specifier is not important; lower or upper case
        # will work.
        self.rotateOldFile()
        currentTime = int(time.time())
        if self.when == 'S':
            self.interval = 1 # one second
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$"
        elif self.when == 'M':
            self.interval = 60 # one minute
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}$"
        elif self.when == 'H':
            self.interval = 60 * 60 # one hour
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}$"
        elif self.when == 'D' or self.when == 'MIDNIGHT':
            self.interval = 60 * 60 * 24 # one day
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        elif self.when.startswith('W'):
            self.interval = 60 * 60 * 24 * 7 # one week
            if len(self.when) != 2:
                raise ValueError("You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s" % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                raise ValueError("Invalid day specified for weekly rollover: %s" % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)

        self.extMatch = re.compile(self.extMatch)
        self.interval = self.interval * interval # multiply by units requested
        self.rolloverAt = self.computeRollover(int(time.time()))

        #print "Will rollover at %d, %d seconds from now" % (self.rolloverAt, self.rolloverAt - currentTime)
        
    def rotateOldFile(self):
        interval = 24 * 60 * 60
        if self.when == 'MIDNIGHT':
            if os.path.exists(self.baseFilename):
                while True:
                    try:
                        with open(self.baseFilename) as f:
                            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                            lastLogTime = os.path.getmtime(self.baseFilename)
                            lastLogDay = time.strftime('%Y-%m-%d',time.localtime(lastLogTime))
                            lastLogDayTime = int(lastLogTime) / interval * interval
                            dfn = self.baseFilename + "." + lastLogDay
                            currentTime = int(time.time())
                            if currentTime - lastLogDayTime > interval and not os.path.exists(dfn):
                                os.rename(self.baseFilename, dfn)
                            fcntl.flock(f, fcntl.LOCK_UN)
                            break
                    except Exception, e:
                        #import traceback
                        #traceback.print_exc()
                        time.sleep(1)
        if self.stream:
            self.stream.close()
            self.stream = self._open()

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        pid = os.getpid()
        if self.stream:
            self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
        dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        
        # fix the muliprocessing error
        #if os.path.exists(dfn):
        #    os.remove(dfn)
        
        while True:
            try:
                with open(self.baseFilename) as f:
                    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    if not os.path.exists(dfn):
                        os.rename(self.baseFilename, dfn)
                    fcntl.flock(f, fcntl.LOCK_UN)
                    break
            except Exception, e:
                #print e
                time.sleep(0.1)

        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                try:
                    os.remove(s)
                except Exception, e:
                    pass

        self.mode = 'a'
        self.stream = self._open()
        currentTime = int(time.time())
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        #If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstNow = time.localtime(currentTime)[-1]
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    newRolloverAt = newRolloverAt - 3600
                else:           # DST bows out before next rollover, so we need to add an hour
                    newRolloverAt = newRolloverAt + 3600
        self.rolloverAt = newRolloverAt

class Logging(object):
    def __init__(self, logfile_name ,logger_name):
        log_dir = os.path.dirname(logfile_name)
        if log_dir:
            if not os.path.exists(log_dir):
                raise Exception("init Logging fail: %s log dir not exist" % log_dir)
        
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        #self.file_handler = logging.handlers.TimedRotatingFileHandler(log_name, 'D', 1, 60)
        #self.file_handler = NewLogHandler(log_name, 'D', 1, 60)
        self.file_handler = NewLogHandler(logfile_name, 'midnight', 1, 60)
        #self.file_handler = NewLogHandler(log_name, 'M', 1, 20)
        #self.file_handler = logging.handlers.RotatingFileHandler(log_name, maxBytes = 5 * 1024 * 1024, backupCount = 10)
        self.file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)
        
    def __del__(self):
        self.file_handler.close()
        
if __name__ == '__main__':
    log_handle1 = Logging('log_test1', 'log_test22')
    processid = os.getpid()
    i = 0
    while i < 10:
        i+=1
        ri = random_test.randint(0, 1000)
        log_handle1.logger.info("(%d)%s" % (processid, ri))
        time.sleep(0.1)
