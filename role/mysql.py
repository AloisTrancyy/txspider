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
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'spider',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}


if __name__ == "__main__":
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        sql = 'select count(1) as count from role where equip_id=179782'
        cursor.execute(sql)
        print(cursor.fetchone()['count'])
        cursor.close()
        connection.close()
