# 内存调查笔记:
pyrasite-shell 11

import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
len(gc.garbage)



apt-get update
apt-get install gdb
pip install  urwid
pip install pyrasite
安装 meliae


pyrasite-memory-viewer 11


# redis 信息
/usr/local/redis/bin/redis-cli -h 192.168.173.117 -p 5000 info | grep instan


"http://www.cnblogs.com/xybaby/p/7491656.html"



# 内存调查笔记
import sys
s = 'asdf'
sys.getrefcounts(s)
2

# 循环引用
1. 
 gc.get_threshold()
 
 gc.collection()
 gc.get_objects()

gc.get_referents(*obj)
gc.get_referrers(*obj)

gc.DEBUG_UNCOLLECTABLE
gc.DEBUG_COLLETABLE


　　第一是对象被另一个生命周期特别长的对象所引用，比如网络服务器，可能存在一个全局的单例ConnectionManager，管理所有的连接Connection，如果当Connection理论上不再被使用的时候，没有从ConnectionManager中删除，那么就造成了内存泄露

　第二是循环引用中的对象定义了__del__函数，这个在《程序员必知的Python陷阱与缺陷列表》一文中有详细介绍，简而言之，如果定义了__del__函数，那么在循环引用中Python解释器无法判断析构对象的顺序，因此就不错处理。



objgraph
def count(typename)
def by_type(typename)
def show_most_common_types(limits = 10)
def show_growth()
def show_backrefs()


objgraph.show_growth()
objgraph.show_most_common_types()


objgraph.show_backrefs(objgraph.by_type('list')[0], max_depth = 10, filename = 'obj.dot')


