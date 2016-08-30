# -*- coding:utf8 -*-
import MySQLdb
from random import randint, random, shuffle
import time
from create_table import mrand, get_sectors

from create_index import raw_str, index_str


def get_one_condition(num_conditions):
    key_word = raw_str.replace(" ", "").replace("\n", "").split(",")
    one_data = (mrand(16), mrand(24), get_sectors(1),
                mrand(8), mrand(8), mrand(8), mrand(8),
                mrand(16), random(), random(), random(),
                mrand(8), random(), mrand(8), mrand(32), mrand(32),
                mrand(8), random(), random(),
                random(), random(), random(), random(),
                mrand(8), mrand(8), random(), random(), random(),
                mrand(64), random(), random(), random(), mrand(8),
                get_sectors(1))
    conditions = map(lambda a, b: (a, b), key_word, one_data)
    str_conditions = []
    for key, value in conditions:
        temp_str = ""
        if key in ("`yy_date`", "`yy_time`", "`flow`"):
            temp_str = key + " > " + str(value)
        elif type(value) == int:
            temp_str = key + " = " + str(value)
        elif type(value) == str:
            temp_str = key + " like \"%" + str(value) + "%\""
        elif type(value) == float:
            temp_str = key + " > " + str(value)
        str_conditions.append(temp_str)
    # 因为查询的时候不会用到stock_id
    str_conditions = str_conditions[0:1] + str_conditions[2:]
    shuffle(str_conditions)
    return str_conditions[:num_conditions]


def run(title="with"):
    db = MySQLdb.connect(user="root", passwd="123456", db="stock")
    cur = db.cursor()
    f = open("%s_index_every_sql.out" % title, "w")
    f_all = open("%s_index_summary.out" % title, "w")
    num_of_tests = 100
    num_of_conditions = 15
    f_all.write("one conditions per test = " + str(num_of_tests) + "\n")
    for num_conditions in range(1, num_of_conditions + 1):
        temp_time = 0
        ans_len = 0
        for num_i in range(num_of_tests):
            str_conditions = get_one_condition(num_conditions)
            t = time.time()
            sql = "select count(*) from history_stock_stat where %s" % " and ".join(str_conditions)
            f.write("sql = " + sql + "\n")
            cur.execute(sql)
            qq_time = time.time() - t
            qq_len = cur.fetchone()
            f.write("length : " + str(qq_len) + " time: " + str(qq_time) + "\n\n")
            temp_time += qq_time
            ans_len += qq_len[0]
        f_all.write("conditions_num = %s , average_time = %s, average_ans_len = %s \n" %
                    (num_conditions, temp_time / num_of_tests, 1.0 * ans_len / num_of_tests))
    f.close()
    db.close()


if __name__ == "__main__":
    run()
