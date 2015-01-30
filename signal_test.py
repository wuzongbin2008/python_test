import os
import sys
import signal
import threading
import logging
import time

total_count = 0
safe_exits = False
processid = os.getpid()

def counter(lock):
    global total_count
    #have_it = lock.acquire(0)

    while True:
        total_count +=1
        print "Thread: %s\ttotal_count = %d\n" % (threading.currentThread().getName(), total_count)
        safe_exit()
        time.sleep(1)
    #lock.release()

def start_threads():
    global total_count
    lock = threading.Lock()

    threads = []
    for i in range(10):
        worker = threading.Thread(target=counter, args=(lock,), name="Worker %d" % i)
        worker.daemon = True
        threads.append(worker)

    for i in range(10):
        threads[i].start()

    for i in range(10):
       threads[i].join()

def signal_handler(signum, frame):
    global safe_exits, processid
    print "enter signal_handler\n"
    if signum in (signal.SIGUSR1, signal.SIGINT, signal.SIGTERM, signal.SIGSEGV):
        print "(%d)receive signal_usr1" % processid
        safe_exits = True

def safe_exit():
    global safe_exits
    #print "enter safe_exit\n"
    if safe_exits:
        print "catch signal, safe exit"
        exit(0)

def set_signal_handler():
    signal.signal(signal.SIGUSR1, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGSEGV, signal_handler)

def main_thread_print():
    i = 0
    while True:
        time.sleep(1)
        print i
        safe_exit()
        i += 1


if __name__ == "__main__":
    #ActivePool_test()
    set_signal_handler()

    #start_threads()
    main_thread_print()

    print "main thread\n"