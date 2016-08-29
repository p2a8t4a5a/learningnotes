# redis 基础用法
exists mykey
append mykey "hellp"
append mykey " asd"
get mykey
strlen mykey

getrange mykey 0 3  # 4 char
getrange mykey -5 -1
setrange mykey 0 "aaa"

set mykey "10"
incrby mykey 5

incrbyfloat mykey 0.1
mget key1 key2 key3


# 原子的
mset key1 "ads" key2 "asd" key3 "asd"

setex = set .. expire 



set mykey "foobar"
bitop and destkey key1 key2 # key的value 
AND 、 OR 、 NOT 、 XOR

setbit key 0 1


lrange key 0 -1
lindex key 0 
lset key 0 "four"  O(n)
linsert mylist before "world" "there""









# set 操作
sadd myset aaa
sadd myset bbb
sadd myset ccc

smembers myset  # 获取集合内容
scard myset #  获取个数 
srem myset aaa # 删除
sinter key1 key2 # 交集

redis做队列的强度。一把来说100w条的队列数据，占用73M 内存左 右。200w条数据内存在154M内存左右。 


# 
用连接池 节约资源
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

sismember myset "one"
sunion 并集



















# 1
# redis 存储对象的一个方法
# import pickle
import cPickle as pickle
rs.set("yao",pickle.dumps({'a':1}))
pickle.loads(rs.get("yao"))

# 2
from redisco import models
class Person(models.Model):
    name = models.Attribute(required = True) # unicode
    counter = models.Counter() # 计数器,Model.incr Model.decr
    # datetimefiled = models.DateTimeField() # DateTime object
    # datefield = models.DateField() # Date object
    floatfield = models.FloatField()
    booleanField = models.BooleanField(1)
    # referencefiled = models.ReferenceField(None)
    # listfield = models.ListField([1,2,3])


# 3
from redisco import models  
class Person(models.Model):  
    name = models.Attribute(required=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    fave_colors = models.ListField(str)  
    
    def add_color(self,color="yellow"):
        self.fave_colors.append(color)

person = Person(name = "yao")
person.save()

person = Person.objects.filter(name = "yao")
        


rs = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
rs.set("yao","1")
rs.get("yao")



# pipe r.pipline(transaction = False)
pipe = r.pipline()
pipe.set("aaa","first")
pipe.set("bbb","second")
pipe.execute()


# 官方推荐安装性能快10倍
pip install hiredis



