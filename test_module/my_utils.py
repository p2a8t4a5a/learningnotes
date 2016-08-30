#! /usr/bin/python
import os
import sys

def freopen(file_path,mode,oldstream):
    """ 类似于C语言的重定向"""
    f=open(file_path,mode)
    newfd=f.fileno()
    oldfd=oldstream.fileno()
    os.close(oldfd)
    os.dup2(newfd,oldfd)

if __name__=="__main__":
    freopen('data.in','a',sys.stdout)
    print 'nihao'
