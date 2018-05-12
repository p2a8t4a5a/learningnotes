# 内存调查笔记:
pyrasite-shell 11

import gc
gc.set_debug(gc.DEBUG_COLLECTABLE)
len(gc.garbage)

gc.set_debug(gc.DEBUG_COLLECTABLE)
len(gc.garbage)



apt-get update
apt-get install  gdb
安装 meliae
pip install  urwid
pip install pyrasite


pyrasite-memory-viewer 11


# redis 信息
/usr/local/redis/bin/redis-cli -h 192.168.173.117 -p 5000 info | grep instan
