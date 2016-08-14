# -*- coding:utf8 -*-
"""
    描述符到一些实例
    
"""


# 最基础到用法
class WebFramework(object):
    def __init__(self,name='Flask'):
        self.name = name

    def __get__(self,instance,owner):
        return self.name
    
    def __set__(self,instance,value):
        self.name = value


class PythonSite(object):
    """ classmethod 和 staticmethod 几乎一样只是一个需要硬编码"""
    web_framework = WebFramework()
    version = 0.1

    def __init__(self,site):
        self.site = site
    
    def get_site(self):
        return self.site

    @classmethod
    def get_version(cls):
        return cls.version
    
    @staticmethod
    def find_version():
        return PythonSite.version



# 描述器实现类中方法到缓存
class _Missing(object):
    def __repr__(self):
        return 'no value'
    
    def __reduce__(self):
        return '_missing'


_missing = _Missing()


class cached_property(object):
    def __init__(self,func,name=None,doc=None):
        print 55,self,func,name,doc
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self,obj,type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__,_missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class Foo(object):
    @cached_property
    def foo(self,name='yaoge'):
        print 'first calculate'
        result = 'this is result'
        return result






# property
class Movie(object):
    def __init__(self,budget=None):
        self._budget = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self,value):
        if value<0:
            raise ValueError('Negative value')
        self._budget = value

    @property
    def total_budget(self):
        return self.budget * 2


from weakref import WeakKeyDictionary
class NonNegative(object):
    def __init__(self,default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self,instance,owner):
        print 'this is get'
        return self.data.get(instance,self.default)

    def __set__(self,instance,value):
        print 'this is set '
        if value<0:
            raise ValueError('Negative value')
        self.data[instance]=value


class Movie(object):

    budget = NonNegative(0)
    
    def __init__(self,budget=0):
        pass
    



class Descriptor(object):
    def __init__(self,label):
        print 'i am label:',label
        self.label = label
        self.data = {}

    def __get__(self,instance,owner):
        print 'get instance',instance,self.label
        print 'self.data: ',self.data
        return instance.__dict__.get(self.label)

    def __set__(self,instance,value):
        print 'set'
        self.data[self.label] = value
        instance.__dict__[self.label] = value


class FooList(list):
    x = Descriptor('x')
    y = Descriptor('y')






# 元类的用法
class Descriptor(object):
    def __init__(self):
        self.label = None

    def __get__(self,instance,owner):
        return instance.__dict__.get(self.label)

    def __set__(self,instance,value):
        instance.__dict__[self.label]=value


class DescriptorOwner(type):
    def __new__(cls,name,bases,attrs):
        print cls
        print name
        print bases
        print attrs
        for n,v in attrs.items():
            if isinstance(v,Descriptor):
                v.label = n
                print n,type(n)
        return super(DescriptorOwner,cls).__new__(cls,name,bases,attrs)


class Foo(object):
    __metaclass__ = DescriptorOwner
    x = Descriptor()


    

class CallbackProperty(object):
    """A property that will alert observers when upon updates"""
    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance==None:
            print self
            return self
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):        
        for callback in self.callbacks.get(instance, []):
            # alert callback function of new value
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """Add a new function to call everytime the descriptor updates"""
        #but how do we get here?!?!
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)
 

class BankAccount(object):
    balance = CallbackProperty(0)

def low_balance_warning(value):
    if value < 100:
        print "You are poor"

 

ba = BankAccount()
ba.balance.add_callback(ba, low_balance_warning)





