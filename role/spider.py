# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import html_downloader
import html_parser
import pymysql.cursors
import traceback

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

    def craw(self, url):
        connection = pymysql.connect(**config)
        try:
            html_cont = self.downloader.download(url)
            new_data = self.parser.parse(html_cont)
            with connection.cursor() as cursor:
                sql = 'INSERT INTO role_basic (role_id'
                for key, value in new_data.items():
                    if key == 'role_id':
                        continue
                    sql = sql + ',' + key
                sql = sql + ' ) values (' + new_data['role_id']
                for key, value in new_data.items():
                    if key == 'role_id':
                        continue
                    if type(value) == int:
                        sql = sql + ',' + str(value)
                    else:
                        sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8"))+'\''

                sql += ')'
                print(sql)
                cursor.execute(sql)
                connection.commit()
        except Exception as e:
            print(e,traceback.print_exc())
        finally:
            connection.close()

urls = [
    "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail&serverid=2&equip_id=150591",
    "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail&serverid=15&equip_id=406192"
]
if __name__ == "__main__":
    root_url = "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail&serverid=15&equip_id=392061"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
