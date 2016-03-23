#! /usr/bin/env python
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',db='school')
cursor=conn.cursor()
#print cursor,6
try:
	sql="select * from test"
	cursor.execute(sql)
	tmp=cursor.fetchone()
	print tmp,9
	tmp=cursor.fetchone()
	print tmp,12
	
	cursor.scroll(-2)
	tmp=cursor.fetchall()
	print tmp	
	
	cursor.scroll(0,mode='absolute')
	print cursor.fetchmany(1)	
except MySQLdb.Error,e:
	print 'error',e.args[0],e.args[1]
conn.close()	
