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



# python官方文档
# https://wiki.python.org/moin/PythonDecoratorLibrary
import time

class cached_property(object):
    '''Decorator for read-only properties evaluated only once within TTL period.

    It can be used to create a cached property like this::

        import random

        # the class containing the property must be a new-style class
        class myclass(object):
            # create property whose value is cached for ten minutes
            @cached_property(ttl=600)
            def randint(self):
                # will only be evaluated every 10 min. at maximum.
                return random.randint(0, 100)

    The value is cached  in the '_cache' attribute of the object instance that
    has the property getter method wrapped by this decorator. The '_cache'
    attribute value is a dictionary which has a key for every property of the
    object which is wrapped by this decorator. Each entry in the cache is
    created only when the property is accessed for the first time and is a
    two-element tuple with the last computed property value and the last time
    it was updated in seconds since the epoch.

    The default time-to-live (TTL) is 300 seconds (5 minutes). Set the TTL to
    zero for the cached value to never expire.

    To expire a cached property value manually just do::

        del instance._cache[<property name>]

    '''
    def __init__(self, ttl=300):
        self.ttl = ttl

    def __call__(self, fget, doc=None):
        print doc
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        return self

    def __get__(self, inst, owner):
        now = time.time()
        try:
            value, last_update = inst._cache[self.__name__]
            if self.ttl > 0 and now - last_update > self.ttl:
                raise AttributeError
        except (KeyError, AttributeError):
            value = self.fget(inst)
            try:
                cache = inst._cache
            except AttributeError:
                cache = inst._cache = {}
            cache[self.__name__] = (value, now)
        return value





class myclass(object):
    # create property whose value is cached for ten minutes
    @cached_property(ttl=600)
    def randint(self,doc="asd"):
        """ will only be evaluated every 10 min. at maximum. """
        return random.randint(0, 100)






