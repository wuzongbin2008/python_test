import logging
import threading
import time
import os
from common import worker2

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)
n = 0

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

def lock_test():
    lock = threading.Lock()
    holder = threading.Thread(target=lock_holder,args=(lock,),name="LockHolder")
    holder.setDaemon(True)
    holder.start()

    worker = threading.Thread(target=lock_worker,args=(lock,),name="Worker")
    worker.start()

def semaphore_test():
    if semaphore.acquire():
        for i in range(5):
          print (threading.currentThread().getName() + ': get semaphore_%d\n' % i)
        semaphore.release()
        print (threading.currentThread().getName() + ' release semaphore')

def daemon():
    logging.debug("Starting")
    time.sleep(12)
    logging.debug("Exiting")

def non_daemon():
    logging.debug("Starting")
    logging.debug("Exiting")

def join_test():
    d = threading.Thread(name="daemon",target=daemon)
    t = threading.Thread(name="non-daemon",target=non_daemon)
    d.start()
    t.start()

semaphore = threading.Semaphore(10)
if __name__ == "__main__":
    join_test()