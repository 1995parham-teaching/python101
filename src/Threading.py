# In The Name Of God
# ========================================
# [] File Name : Threading
#
# [] Creation Date : 15-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import threading
import time


class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        lock.acquire()
        print_time(self.name, self.counter, 5)
        lock.release()
        print("Exiting " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
lock = threading.Lock()

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")