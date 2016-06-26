#! /usr/bin/env python
import MySQLdb

#mysql connect charset='gb2312' ='utf8'
db=MySQLdb.connect(host="localhost",user="root",passwd="",db="school")
cursor =db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print data

#create table
cursor.execute("DROP table if exists test")
sql="""create table test (
	no char(10) primary key,
	name char(10) not null)
"""
cursor.execute(sql)

#insert data
sql="""
	insert into test(no,name) 
values("%s",'%s')
"""
try:
	cmd=sql%('YY','1111')
	cursor.execute(cmd)
	cmd=sql%('ZZ','2222')
	cursor.execute(cmd)	
	#cur.executemany('insert into test values(%s,%s)',values)
except:
	db.rollback()
	print 'error'

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


