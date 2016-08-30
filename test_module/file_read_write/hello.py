#! /usr/bin/python
import os
import sys


if len(sys.argv)>1:
    fd=int(sys.argv[1])
    print 'fd',fd
    os.write(fd,'nihao')

print 'hellp'

