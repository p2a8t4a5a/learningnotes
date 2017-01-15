import MySQLdb
import time

db = MySQLdb.connect(user="root", passwd="123456", db="stock")
cur = db.cursor()
t = time.time()
sql = "select \"%s\" from history_stock_stat WHERE 1 limit 1" % ("1"*10000000)
print len(sql)
cur.execute(sql)
ans = cur.fetchall()
print len(ans[0][0])
print time.time()-t

