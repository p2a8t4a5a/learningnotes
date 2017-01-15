#! /usr/bin/python
# -*- coding:UTF-8 -*-
import threading
import time
from work import start_work
import sys

def multi_thread_test(func, n, *args, **kwargs):
    """ 运行n次 """
    t = time.time()
    for i in range((n+num_process-1)/num_process):
        threads=[None]*min(num_process, n-num_process*i)
        print len(threads),
        for j in range(len(threads)):
            threads[j]=threading.Thread(target=func,args=args,kwargs=kwargs)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    print '\nmulti_thread_test time =', time.time() - t


if __name__ == '__main__':
    num = int(sys.argv[1])
    global num_process
    num_process = int(sys.argv[2])
    multi_thread_test(start_work,num)
