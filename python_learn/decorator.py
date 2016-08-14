# -*- coding:utf8 -*-


# 带参数的装饰器
def deco(arg,arg2):
    print 'deco start'
    def _deco(func):
        print '_deco start'
        def __deco(*args,**kwargs):
            print 'args',arg,arg2
            func(*args,**kwargs)
            print 'args',func
        print '_deco end'
        return __deco
    print 'deco end'
    return _deco

def deco2(arg,arg2):
    print 'deco2 start'
    def _deco(func):
        print '_deco2 start'
        def __deco(*args,**kwargs):
            print 'args2',arg,arg2
            func(*args,**kwargs)
            print 'args2',func
        print '_deco2 end'
        return __deco
    print 'deco2 end'
    return _deco


@deco2(arg="yes2",arg2="no2")
@deco(arg="yes",arg2="no")
def show(name):
    print "i am ",name
            




# 带类得装饰器
class Foo(object):
    def __init__(self,func):
        self._func = func

    
    def __call__(self,*args,**kwargs):
        print 'before'
        self._func(*args,**kwargs)
        print 'end'

@Foo
def show(name):
    print name




# 类中装饰器
def cached_method(flush_time):
    def _cached(func):
        def __cached(*args,**kwargs):
            print 'before'
            print flush_time
            func(*args,**kwargs)
            print 'end'
        return __cached
    return _cached



class A(object):
    @cached_method(123)
    def show(self,name):
        print 'i am',name




https://wiki.python.org/moin/PythonDecoratorLibrary











