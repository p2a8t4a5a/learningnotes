# -*- coding:utf8 -*-
import MySQLdb
from random import randint, random

raw_str = """`days`, `stock_id`, `sectors`, `report_level`,
    `network_level`, `stock_news`, `sector_news`, `ltg`, `ltsz`, `sy_rate`,
    `sj_rate`, `yg_type`, `yjyg_rate`, `yjyg_type`, `yy_date`, `yy_time`,

     `yy_type`, `jlrtb_rate`, `ystb_rate`, `mgjzc`, `mgsy`, `jzcsy_rate`,
     `jlr_rate`, `yj_types`, `gszyq`, `price`, `rate`, `turnover`,
     `flow`, `flow_rate`, `yzyqyec_rate`, `rzrqyec_change`,
      `flow_control`, `zb` """

index_str = """`yy_type`, `jlrtb_rate`, `ystb_rate`, `mgjzc`, `mgsy`, `jzcsy_rate`,
     `jlr_rate`, `yj_types`, `gszyq`, `price`, `rate`, `turnover`,
     `flow`, `flow_rate`, `yzyqyec_rate`, `rzrqyec_change`,
      `flow_control`, `zb`"""


def run():
    db = MySQLdb.connect(user="root", passwd="123456", db="stock")
    cur = db.cursor()
    t = 1
    for name in index_str.replace("`", "").replace(" ", "").replace("\n", "").split(","):
        create_index_sql = "ALTER TABLE `history_stock_stat` ADD INDEX index_%s (`%s`) " % (name, name)
        cur.execute(create_index_sql)
        print t
        t += 1
        db.commit()
    db.close()


if __name__ == "__main__":
    run()
