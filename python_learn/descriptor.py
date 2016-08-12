# -*- coding:utf8 -*-

class WebFramework(object):
    def __init__(self,name='Flask'):
        self.name = name

    def __get__(self,instance,owner):
        return self.name
    
    def __set__(self,instance,value):
        self.name = value


class PythonSite(object):
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


class _Missing(object):
    def __repr__(self):
        return 'no value'

    
    def __reduce__(self):
        return '_missing'


_missing = _Missing()


class cached_property(object):
    def __init__(self,func,name=None,doc=None):
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
    def foo(self):
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
    
