
# 1.divide
from __future__ import division
1/2 = 0.5
1//2=0

# 2.input
x=input("asd")
y=raw_input("dasd") #just like gets()


# 3. math and cmath
import math
math.floor(1.1)
# do something more
import cmath 


# 5. r 
print r'C:\\desktop' 
#out:   C:\\desktop


# 6 左闭右开
yaoge=[1,2,3,4]
yaoge[3::-1] 


# 7
'y' in 'aay'

# 8 输出格式控制
print '%-10.3f' % 3.32 #left algin
print '%010.3f' % 3.32 #fill with zero
print '%*s' % (12,'asd')

# 9 替换
from string import maketrans
table=maketrans("ab","cd")
'apple boy'.translate(table,' ')#translate'a' and 'b' and delete ' '

# 10 find the value'as' not as
item = {'as':123}
print " %(as)s" % item 
print " {as}".format(**item)

# 11
for k,v in my_dict.iteritems():
    print k,v

# 12 enumerate
for index,string in enumerate(strings):
	print index,string
	if(index==3):break

# 13 exec and eval
scope={}
exec("x=1",scope)
ans = eval("x+1",scope)

# 14 choice
from random import choice
choice([1,2])

# 15
class Person():
	def __secret(self):
		print 'it is secret'

a = Person()
a._Person__secret()


# 16 类继承的一些用法
class Filter:
	def init(self):
		self.blocked=[]
	def filter(self,seq):
		return [x for x in seq if x not in self.blocked]
	
class SpamFilter(Filter):
	def init(self):
		self.blocked=['SPAM']

issubclass(SpamFilter,Filter)
SpamFilter.__base__
isinstance(a,SpamFilter)

class C(A,B) #multi inherit

hasattr(SpamFilter,'init')
callable(getattr(SpamFilter,'init',None))
setattr(a,'calc',lambda self,x:x*x)


# 17 call the super
class A(B):
	def __init__(self,name='yaoge'):
		B.__init__(self) #super(A,self).__init__()
		self.name=name










































