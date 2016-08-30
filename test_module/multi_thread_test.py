#! /usr/bin/python
# -*- coding:UTF-8 -*-
import threading
import time


def multi_thread_test(func, n_out, n_in, *args, **kwargs):
    """n_in 内层次数 n_out 外层次数"""
    t = time.time()
    print 'multi_thread_test start:'
    for i in xrange(n_out):
        threads=[None]*n_in
        for j in xrange(n_in):
            threads[j]=threading.Thread(target=func,args=args,kwargs=kwargs)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    print 'multi_thread_test time =', time.time() - t


def multi_thread_test_with_i(func, n_out, n_in, *args, **kwargs):
    """n_in 内层次数 n_out 外层次数"""
    t = time.time()
    print 'multi_thread_test start:'
    for i in xrange(n_out):
        threads = [None] * n_in
        for j in xrange(n_in):
            mykwargs=kwargs.copy()
            mykwargs['i'] = j
            threads[j] = threading.Thread(target=func, args=args, kwargs=mykwargs)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    print 'multi_thread_test time =', time.time() - t


if __name__ == '__main__':
    def print_test(a,b):
        print a+b
    multi_thread_test(print_test,2,5,1,b=2)

