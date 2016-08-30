#! /usr/bin/python
import os
import signal
import time
import sys
"""
python 中的信号的用法
"""

def handler(sig,frame):
    if sig==signal.SIGTERM:
        sys.exit(0)
    sys.exit(1)

def test():
    signal.signal(signal.SIGTERM,handler)
    time.sleep(10)
    print 'ends'

def test2():
    print 'start program'
    signal.signal(signal.SIGTERM,handler)
    pid=os.fork()
    if pid==0:
        print 'i am child',pid,os.getpid()
        #os.setsid()
        time.sleep(5)
        os.kill(os.getppid(),signal.SIGTERM)
    elif pid>0:
        print 'i am parent',os.getpid(),'my son',pid
        time.sleep(10)
        sys.exit(0)
    for i in range(5):
        time.sleep(5)
        with open('data.in','a') as f:
            f.write('hello\n')

if __name__=="__main__":
    #test()
    test2()
    print 'haha'
