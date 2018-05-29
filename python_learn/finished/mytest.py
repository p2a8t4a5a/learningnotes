#! /usr/bin/env python
import MySQLdb
import sys
from time import sleep

#mysql connect charset='gb2312' ='utf8'
db=MySQLdb.connect(host="localhost",user="root",passwd="",db="yydd", autocommit=False)
cursor =db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print data

#create table
# cursor.execute("DROP table if exists test")
# sql="""create table test (
# id int unsigned primary key,
# score int not null)
# """
# cursor.execute(sql)


cursor.execute("select score from test where id = 1 for update")
ans=cursor.fetchone()[0]

sql="""
        update test set score = score - 10 where id =1;
"""
try:
        print cursor.execute(sql)
        sleep(15)
        print cursor.execute(sql)
        sleep(15)
except:
        db.rollback()
        print 'error'

db.commit()

sys.exit(0)

#query 
sql="""
	select * from test
"""
try:
	cursor.execute(sql)
	tmp= cursor.fetchall()
	#res=cursor.fetchmany(5)
	#cursor.scroll(0,mode='absolute')
	#cursor.scroll(-2,mode='relative')	
	print tmp
	print cursor.rowcount
except:
	print 'error 43'

#update
sql="""
	update test set name='aaa' where no='YY'
"""
try:
	cursor.execute(sql)
except:
	print 'error 51'
	db.rollback()
	
#zhixing shiwu


db.commit()
db.close()


