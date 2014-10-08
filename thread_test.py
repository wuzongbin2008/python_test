import logging
import threading
import time
import os
import datetime
from common import worker2

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s (%(threadName)-10s) %(message)s',)
n = 0
total_count = 0
#semaphore = threading.Semaphore(10)

def lock_holder(lock):
    logging.debug("Starting")
    while True:
        lock.acquire()
        try:
            logging.debug("holding")
            time.sleep(0.5)
        finally:
            logging.debug("not holding")
            lock.release()
        time.sleep(0.5)
    return

def lock_worker(lock):
    logging.debug("Starting")
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug("trying to acquire")
        have_it = lock.acquire(0)
        try:
            num_tries +=1
            if have_it:
                logging.debug("iteration %d : Acquired\n",num_tries)
                num_acquires +=1
            else:
                logging.debug("iteration %d : Not Acquired",num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug("Done after %d iterations",num_tries)

def counter(lock):
    global total_count
    logging.debug("Starting")
    #have_it = lock.acquire(0)
    total_count +=1
    #lock.release()
    logging.debug("total_count = %d",total_count)

def lock_test():
    global total_count
    lock = threading.Lock()
    # holder = threading.Thread(target=lock_holder,args=(lock,),name="LockHolder")
    # holder.setDaemon(True)
    # holder.start()
    threads = []
    for i in range(10):
        worker = threading.Thread(target=counter,args=(lock,),name="Worker %d" % i)
        threads.append(worker)

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()

    logging.debug("total_count = %d",total_count)

# def semaphore_test():
#     if semaphore.acquire():
#         for i in range(5):
#           print (threading.currentThread().getName() + ': get semaphore_%d\n' % i)
#         #semaphore.release()
#     print (threading.currentThread().getName() + ' release semaphore')

def daemon():
    global n
    logging.debug("%d Starting" % datetime.datetime.now().time().microsecond)
    time.sleep(3)
    logging.debug("%d Exiting" % datetime.datetime.now().time().microsecond)
    n +=1
    logging.debug("n = %d\n" % n)
    #print "daemon n = %d\n" % n

def non_daemon():
    global n
    logging.debug("%d Starting" % datetime.datetime.now().time().microsecond)
    logging.debug("%d Exiting" % datetime.datetime.now().time().microsecond)
    n +=1
    logging.debug("n = %d\n" % n)

def join_test():
    d = threading.Thread(name="daemon",target=daemon)
    t = threading.Thread(name="non-daemon",target=non_daemon)
    d.start()
    t.start()
    d.join()
    t.join()

def print_t():
    print "ok"

class ActivePool(object):
    def __init__(self):
        super(ActivePool,self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self,name):
        with self.lock:
            self.active.append(name)
            logging.debug("Running:%s",self.active)
    def makeInactive(self,name):
        with self.lock:
            self.active.remove(name)
            logging.debug("Running:%s",self.active)

def worker(s,pool):
    logging.debug("Waiting to join the pool")
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

def ActivePool_test():
    pool = ActivePool()
    s = threading.Semaphore(2)
    for i in range(4):
        t = threading.Thread(target=worker,name=str(i),args=(s,pool))
        t.start()

if __name__ == "__main__":
    #ActivePool_test()
    lock_test()
