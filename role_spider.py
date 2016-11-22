# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import time
import traceback
import configparser
import logging
import pymysql
from role import html_downloader
from role import html_parser
from role import url_manager
from apscheduler.schedulers.blocking import BlockingScheduler


config = configparser.ConfigParser()
config.read("config.ini")
dbconfig = {
    'host': config.get('mysql', 'host'),
    'port': config.getint('mysql', 'port'),
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'db': config.get('mysql', 'db'),
    'charset': config.get('mysql', 'charset'),
    'cursorclass': pymysql.cursors.DictCursor
}
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='role_spider.log',
                    filemode='w')
logger = logging.getLogger('role_spider')

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.urlManager = url_manager.UrlManager()

    def craw(self):
        while (self.urlManager.has_new_url()):
            time.sleep(2)
            url = self.urlManager.get_new_url()
            print(url)
            for key in url.split('&'):
                if 'equip_id' in key:
                    equip_id = key[9:len(key)]
            html_cont = self.downloader.download(url)
            basic_data = self.parser.parse(html_cont, equip_id)
            connection = pymysql.connect(**dbconfig)
            try:
                with connection.cursor() as cursor:
                    query = 'select count(1) as count from role_data where role_id=' + str(equip_id)
                    cursor.execute(query)
                    if cursor.fetchone()['count'] == 0:
                        sql = 'INSERT INTO role_data (role_id'
                        for key, value in basic_data.items():
                            if key == 'role_id' or value is None:
                                continue
                            sql = sql + ',' + key
                        sql = sql + ' ) values (' + basic_data['role_id']
                        for key, value in basic_data.items():
                            if key == 'role_id' or value is None:
                                continue
                            if type(value) == int or type(value) == float:
                                sql = sql + ',' + str(value)
                            else:
                                sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''
                        sql += ')'
                        print(sql)
                        logger.error(sql)
                        update_craw = 'update role set  craw = 1 where role_id = ' + str(equip_id)
                        cursor.execute(sql)
                        cursor.execute(update_craw)
                    connection.commit()
            except Exception as e:
                print(e, traceback.print_exc())
                logging.exception(e)
            finally:
                connection.close()

if __name__ == "__main__":
    obj_spider = SpiderMain()
    connection = pymysql.connect(**dbconfig)
    with connection.cursor() as cursor:
        sql = 'select url from role where yn=1 and craw = 0'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            obj_spider.urlManager.add_new_url(row['url'])
    cursor.close()
    connection.close()
    obj_spider.craw()


