#! /usr/bin/python
# -*- coding:utf-8 -*-

import fcntl
import stat
import os
import sys
import time


def file_test():
    file_path='data.in'
    try:
        fd=os.open(file_path,os.O_RDWR|os.O_CREAT,
                   stat.S_IRUSR | stat.S_IWUSR)
    except OSError as e:
        print 15,e
        sys.exit(1)

    # 如果执行exec时，关闭fd.
    # 因为当执行exec时，fork时父进程或者子程序就被完全替换掉。
    # 但是你的fd没关掉，特别时有些复杂情况不适合手动关掉。
    # 通过此方法会自动帮你关闭fd
    flags=fcntl.fcntl(fd,fcntl.F_GETFD)
    assert flags!=-1
    flags|=fcntl.FD_CLOEXEC
    r=fcntl.fcntl(fd,fcntl.F_SETFD,flags)
    assert r!=-1

    try:
        # 互斥锁定 #无法建立锁定时，此操作可不被阻断，马上返回进程
        # os.SEEK_SET - 文件的开头， 可以用 0 代替
        fcntl.lockf(fd,fcntl.LOCK_EX|fcntl.LOCK_NB,
                    0,0,os.SEEK_SET)
    except IOError as e:
        print 31,e
        sys.exit(1)
        return -1
    #清空
    os.ftruncate(fd,0)
    os.write(fd,bytes('123456'))
    return 0


def normal_file():
    f=open('data.in','w')
    f.write('normal')
    f.close()


def test_without_lock():
    fd=os.open('data.in',os.O_RDWR|os.O_APPEND|os.O_CREAT)
    for i in range(3):
        pid=os.fork()
        if pid==0:
            t=i
            break
        else:
            t=4
    try:
        # 同一个进程才有效 非强制
        fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB,
                0, 0, os.SEEK_SET)
    except IOError:
        print 'error'
        sys.exit(0)
    os.write(fd,bytes(str(t)+' yaoge'+'\n'))
    os.close(fd)

if __name__ == "__main__":
    test_without_lock()
    # normal_file()
    # file_test()

