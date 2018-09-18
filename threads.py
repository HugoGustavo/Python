import _thread
import time

def print_time1(thread_name, delay):
    count = 0;
    while ( count < 5 ):
        time.sleep(delay);
        count+=1;
        print("%s: %s" % (thread_name, time.ctime(time.time())));

try:
    _thread.start_new_thread(print_time, ("Thread-1", 2, ));
    _thread.start_new_thread(print_time, ("Thread-2", 4, ));
except:
    print('Error: unable to start thread');

#while(1):
  #  pass

import threading
import queue

exitFlag = 0;

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self);
        self.threadID = threadID;
        self.name = name;
        self.q = q;
    
    def run(self):
        print("Starting ", self.name);
        process_data(self.name, self.q);
        print("Exiting " + self.name);
    
def process_data(threadName, q):
    while (not exitFlag):
        queueLock.acquire()
        if ( not workQueue.empty() ):
            data = q.get()
            queueLock.release()
            print( "%s processing %s" % (threadName, data));
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"];
nameList = [ "One", "Two", "Three", "Four", "Five"];