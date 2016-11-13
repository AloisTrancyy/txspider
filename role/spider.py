# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import html_downloader
import html_parser
import url_manager
import pymysql.cursors
import traceback
import time

config = {
    'host': '10.168.66.173',
    'port': 3306,
    'user': 'sellmall',
    'password': 'sellmall1234',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}


class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.urlManager = url_manager.UrlManager()

    def craw(self):
        while (self.urlManager.has_new_url()):
            time.sleep(5)
            url = self.urlManager.get_new_url()
            print(url)
            for key in url.split('&'):
                if 'equip_id' in key:
                    equip_id = key[9:len(key)]
            html_cont = self.downloader.download(url)
            basic_data, calc_data = self.parser.parse(html_cont, equip_id)
            print(basic_data)
            print(calc_data)
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    query = 'select count(1) from role_basic where role_id=' + str(equip_id)
                    count = cursor.execute(query)
                    if count == 0:
                        sql = 'INSERT INTO role_basic (role_id'
                        for key, value in basic_data.items():
                            if key == 'role_id' or value is None:
                                continue
                            sql = sql + ',' + key
                        sql = sql + ' ) values (' + basic_data['role_id']
                        for key, value in basic_data.items():
                            if key == 'role_id' or value is None:
                                continue
                            if type(value) == int:
                                sql = sql + ',' + str(value)
                            else:
                                sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''
                        sql += ')'
                        print(sql)
                        cursor.execute(sql)
                    query = 'select count(1) from role_calc where role_id=' + str(equip_id)
                    count = cursor.execute(query)
                    if count == 0:
                        calcsql = 'INSERT INTO role_calc (role_id'
                        for key, value in calc_data.items():
                            if key == 'role_id' or value is None:
                                continue
                            calcsql = calcsql + ',' + key
                        calcsql = calcsql + ' ) values (' + calc_data['role_id']
                        for key, value in calc_data.items():
                            if key == 'role_id' or value is None:
                                continue
                            if type(value) == int:
                                calcsql = calcsql + ',' + str(value)
                            else:
                                calcsql = calcsql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''

                        calcsql += ')'
                        print(calcsql)
                        cursor.execute(calcsql)
                    connection.commit()
            except Exception as e:
                print(e, traceback.print_exc())
            finally:
                connection.close()


if __name__ == "__main__":
    obj_spider = SpiderMain()
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        sql = 'select equip_id,url from role '
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            obj_spider.urlManager.add_new_url(row['url'])
    cursor.close()
    connection.close()
    obj_spider.craw()
