#! /usr/bin/python
# -*- encoding:utf-8 -*-
import sqlite3

if __name__ == "__main__":
    # connect
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # create table
    cursor.execute('DROP TABLE IF EXISTS scraper')
    create_table_sql = """ create table scraper(
      title CHAR (255),
      author char (255),
      post_at DATETIME_INTERVAL_CODE ,
      content CHAR VARYING ,
      img_url CHAR (255),
      comment_count INT
    );
    """
    cursor.execute(create_table_sql)

    # insert data
    insert_sql="""
        insert into scraper VALUES (?,?,?,NULL ,?,?);
    """
    data=('a','b','c','e',99)
    cursor.execute(insert_sql,data)
    conn.commit()

    # read
    cursor.execute('select * from scraper')
    print cursor.fetchall()

