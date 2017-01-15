#!/usr/bin/python
# -*- coding:utf-8 -*-
import gevent
from gevent import monkey
import time
monkey.patch_all()


def gevent_test(func, n_out, n_in, *args, **kwargs):
    """n_in 内层次数 m_out 外层次数"""
    t=time.time()
    print 'gevent_test start:'
    gevent_list=[]
    for i in xrange(n_out):
        for j in xrange(n_in):
            gevent_list.append(gevent.spawn(func,*args,**kwargs))
        gevent.joinall(gevent_list)
    print 'gevent_test time =',time.time()-t

if __name__ == "__main__":
    def print_test(a,b):
        print a+b
    gevent_test(print_test, 1, 5, 1, 2)


