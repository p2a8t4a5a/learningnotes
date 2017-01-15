#! /usr/bin/python
# -*- coding:UTF-8 -*-
import multiprocessing 
import time
import sys
from work import start_work


def multi_process_test(func, n, *args, **kwargs):
    """ 运行n次 """
    t = time.time()
    for i in range((n+num_process-1)/num_process):
        processes=[None]*min(num_process, n-num_process*i)
        print len(processes),
        for j in range(len(processes)):
            processes[j]=multiprocessing.Process(target=func,args=args,kwargs=kwargs)
        for process in processes:
            process.start()
        for process in processes:
            process.join()
    print '\nmulti_process_test time =', time.time() - t


if __name__ == '__main__':
    num = int(sys.argv[1])
    global num_process
    num_process = int(sys.argv[2])
    multi_process_test(start_work,num)
