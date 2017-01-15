import gevent
from gevent import monkey
monkey.patch_all()
import  time

def test():
    t=time.time()
    from myclient import post
    a=[]

    for k in range(10):
        for i in range(1000):
            a.append(gevent.spawn(post,i,1111))
        gevent.joinall(a)
    print 'total time',time.time()-t

def test2():
    n = 10 ** 7
    t = time.time()
    a = [1] * n
    print time.time() - t
    t = time.time()
    for i in xrange(n):
        a[i] = 1
    print time.time() - t


if __name__=="__main__":
    #test()
    test2()
