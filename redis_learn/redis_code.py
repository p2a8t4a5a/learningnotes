# -*- coding:utf8 -*-
import redis
import MySQLdb
import time

"""
注意事项:
    这里的range 和 python 自带的range是不一样的 0 3 表示 0,1,2,3


"""


def lock_and_run(r, _run, *args, **kwargs):
    """简单锁"""
    lockA = False  # 获取A锁
    if r.getset("lockAkey", True):
        if r.get("lockAvalue") == "zjf":
            lockA = True  # 已锁，且是自己锁的，自己可以打开，避免锁上后进程挂了死锁
    else:
        r.set("lockAvalue", "zjf")
        lockA = True  # 未锁，则直接锁上，并记录是自己上的锁
    if lockA:
        _run(*args, **kwargs)  # 得到锁后运行，运行结束后释放锁
        r.set("lockAkey", False)
        r.set("lockAvalue", "done")
    return lockA


def get_sql_result(cur, sql):
    cur.execute(sql)
    return cur.fetchall()


def update_all_property(cur, rs, schema_name="", table_name="", primary_key_name="id"):
    """ 存储键值的规则 统一用"."来连接, 如 web_stock.stock_rate.600199
                     对于每一项 用散列表来存储"""
    full_table_name = schema_name + "." + table_name
    table_head = [item[0] for item in get_sql_result(cur,
                                                     "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s' and table_schema = '%s';" % (
                                                         table_name, schema_name))]
    for i_num in range(len(table_head)):
        if table_head[i_num] == primary_key_name:
            primary_key_id = i_num
            break
    else:
        primary_key_id = 0
    # 这里不用支持事物
    # f = open("data.out","w")
    pipe = rs.pipeline(transaction=False)

    t1 = time.time()
    table_result = get_sql_result(cur, "select * from %s ;" % full_table_name)
    print time.time()-t1

    for item in table_result:
        for i_num in range(len(item)):
            pipe.hset(full_table_name + "." + str(item[primary_key_id]), table_head[i_num], item[i_num])
            # f.write("   ".join([full_table_name + "." + str(primary_key_id), table_head[i_num], str(item[i_num]),"\n"]))
    pipe.execute()
    # f.close()


def update_one_property():
    pass


def run():
    # 看到有博客建议用连接池 节约资源
    pool = redis.ConnectionPool(host='dblocal', port=6379, db=0)
    rs = redis.StrictRedis(connection_pool=pool)
    # rs = redis.Redis(connection_pool=pool)
    connection = MySQLdb.connect(host="10.47.117.105", user="develop", passwd="123456")
    cur = connection.cursor()
    t0 = time.time()
    update_all_property(cur, rs, "web_stock", "stock_rate", "id")
    print time.time() - t0
    show_result(rs, "web_stock", "stock_rate", "600000")


def show_result(rs, schema_name="", table_name="", key=""):
    print rs.hgetall(".".join([schema_name, table_name, key]))


if __name__ == "__main__":
    run()
    pass
    # for item in data:
    #     rs.delete(prefix + str(item[0]))
    #     for subitem in item:
    #         rs.rpush(prefix + str(item[0]), subitem)
    # print rs.lrange(prefix + "1", 0, -1)
    # print rs.lindex(prefix + "1", 1)
    #
    # # rs = (host='127.0.0.1', port=6379, db=0)
    #
    # pass
