#! /usr/bin/python
# -*- coding:UTF-8 -*-

def start_work(n=2*10**6):
    sum = 0
    for i in xrange(n):
        sum+=i*i*i
    return sum    

