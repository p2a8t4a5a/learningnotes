# -*- coding:utf8 -*-
import MySQLdb
from random import randint, random


# 位数
def mrand(n):
    return randint(0, 2 ** (n - 1) - 1)


def get_sectors(max_n=10):
    n = randint(1, min(10, max_n))
    sectors = set()
    for i in range(n):
        sectors.add(randint(1000, 3000))
    return ",".join([str(item) for item in sectors])


def create_table():
    db = MySQLdb.connect(user="root", passwd="123456", db="stock")
    cur = db.cursor()
    # clean
    cur.execute("delete from `history_stock_stat`")
    db.commit()
    sql = """
    INSERT INTO `history_stock_stat` (`days`, `stock_id`, `sectors`, `report_level`,
    `network_level`, `stock_news`, `sector_news`, `ltg`, `ltsz`, `sy_rate`,
    `sj_rate`, `yg_type`, `yjyg_rate`, `yjyg_type`, `yy_date`, `yy_time`,
     `yy_type`, `jlrtb_rate`, `ystb_rate`, `mgjzc`, `mgsy`, `jzcsy_rate`,
     `jlr_rate`, `yj_types`, `gszyq`, `price`, `rate`, `turnover`,
     `flow`, `flow_rate`, `yzyqyec_rate`, `rzrqyec_change`,
      `flow_control`, `zb`) VALUES
    """
    # 4000 * 3 * 200
    data = []
    for days in range(3 * 200):
        for stock_id in range(4000):
            data.append(
                (days, stock_id, get_sectors(),
                 mrand(8), mrand(8), mrand(8), mrand(8),
                 mrand(16), random(), random(), random(),

                 mrand(8), random(), mrand(8), mrand(32), mrand(32),
                 mrand(8), random(), random(),
                 random(), random(), random(), random(),

                 mrand(8), mrand(8), random(), random(), random(),
                 mrand(64), random(), random(), random(), mrand(8),
                 get_sectors()
                 )
            )
        sql_tmp = sql
        for item in data:
            str_temp = "(" + ",".join(map(lambda a: str(a) if type(a) != str else "\"" + a + "\"", item)) + "),"
            sql_tmp += str_temp
        # print sql
        cur.execute(sql_tmp[:-1])
        db.commit()
        data = []
        print "finished day", days

    # print len(data[0])
    pass


if __name__ == "__main__":
    create_table()
    pass
