#! /usr/bin/python
# -*- encoding:utf-8 -*-
import random
import requests
from BeautifulSoup import BeautifulSoup
import collections
import re
import gevent
import sqlite3
from gevent import monkey

monkey.patch_all()


# 本爬虫通过产生一个给定范围内的数字，来随机爬取一篇文章的信息
# 因为主要消耗是在IO上，所以这里我选用了协程，而不是多线程

class WallStreetCnScraper(object):
    # 协程数组的大小，用来调优
    def __init__(self, num, size_of_gevent_list=20):
        # 待爬取文章队列
        self.wait_article_urls = collections.deque()

        # 对已经爬到的文章url的记录,防止重复
        self.used_article_urls = set()

        self.num = num
        assert self.num >= 0
        self.finished = 0
        self.size_of_gevent_list = size_of_gevent_list
        self._db_init()

    def _db_init(self):
        # connect
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

        # create table
        create_table_sql = """
             create table if not exists scraper(
             title CHAR (255),
             author char (255),
             post_at DATE ,
             content CHAR VARYING ,
             img_url CHAR (255),
             comment_count INT
           );
           """
        self.cursor.execute(create_table_sql)

    # 似乎自动转换为unicode 所以不需要转换
    def _write_to_db(self, title, author, post_at,
                     content, img, comment_count):
        # insert data
        insert_sql = """
                insert into scraper VALUES (?,?,?,?,?,?);"""
        data = (title, author, post_at, content, img, comment_count)

        self.cursor.execute(insert_sql, data)
        self.conn.commit()

    def _run(self, url, call_back=None):
        if url in self.used_article_urls:
            return
        self.used_article_urls.add(url)

        # raw_html = open('test.html').read()
        response = requests.get(url)
        if response.status_code == 200:
            raw_html = response.content
        else:
            return
        try:
            # parse url
            soup = BeautifulSoup(raw_html)
            # get article
            article = soup.body.find(re.compile('^div$'),
                                     attrs={'id': 'main', 'class': 'page-article'}).article

            ans_title = article.h1.string
            meta = article.find('div',
                                attrs={'class': 'meta'})
            ans_author = meta.find('span',
                                   attrs={'class': 'item author'}).text
            ans_post_at = meta.find('span',
                                    attrs={'class': 'item time'}).text
            content = article.find('div',
                                   attrs={'class': 'article-content'})
            ans_content = content.text
            ans_img = content.find('img')
            if ans_img:
                ans_img = ans_img.get('src')
            else:
                ans_img = "Null"
            # get comment
            left_bar = soup.body.find('aside', id='leftbar')
            ans_comment_count = left_bar.div.a.find('span', attrs={'class': 'wscn-cm-counter'}).text
        except AttributeError:
            print 'error line 94 the website is not common'
            return

        # 在这里确定是否超过定下的目标即可
        if self.finished < self.num and callable(call_back):
            self.finished += 1
            call_back(ans_title, ans_author, ans_post_at, \
                      ans_content, ans_img, ans_comment_count)

    def _generate(self, n=20):
        for i in range(n):
            self.wait_article_urls.append(
                'http://wallstreetcn.com/node/' + str(random.randint(0, 245723))
            )

    def run(self):
        while self.finished < self.num:
            # 因为有些网址是无效的，所以不能固定生成确定的大小
            # 改为每次生成一定数量的大小
            self._generate(self.size_of_gevent_list)
            gevent_list = []
            while len(self.wait_article_urls) > 0:
                url = self.wait_article_urls.popleft()
                gevent_list.append(
                    gevent.spawn(self._run, url, self._write_to_db))
            gevent.joinall(gevent_list)
            print self.finished


def show():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scraper;')
    ans = cursor.fetchall()
    for i in ans:
        print i[0]
    print 'total len', len(ans)


# 100个网址用时 74s
# 300个网址用时 221s
if __name__ == "__main__":
    import time

    t = time.time()
    # 300 总网址数
    # 20 协程数组的大小，用来调优
    scraper = WallStreetCnScraper(30, 40)
    scraper.run()
    # show result
    show()
    print '用时', time.time() - t
