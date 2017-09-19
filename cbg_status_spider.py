# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import time
import datetime
import requests
import json
import pymysql
import config
from apscheduler.schedulers.blocking import BlockingScheduler


class StatusSpider(object):
    def back_data(self):
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        config.log_error("back data job start! time = " + today)
        connection = pymysql.connect(**config.dbconfig)
        with connection.cursor() as cursor:
            sql = "select count(1) as count from cbg_role where yn =0"
            cursor.execute(sql)
            res = cursor.fetchone()
            if res['count'] > 5000:
                role_sql = 'select role_id,jiahu,name,server_id,price,url,date_format(exp_time,\'%Y-%c-%d %h:%i:%s\') exp_time ' \
                           'from cbg_role where yn =0'
                config.log_info(role_sql)
                cursor.execute(role_sql)
                roles = cursor.fetchall()
                f_role = open(config.profile_config.get('mysql', 'back_path') + "role_" + today + ".txt", "w")
                f_role.write(str(roles))

                role_data_sql = 'select * from cbg_data where role_id in (select id from cbg_role where yn= 0)'
                cursor.execute(role_data_sql)
                row_datas = cursor.fetchall()

                f_data = open(config.profile_config.get('mysql', 'back_path') + "role_data_" + today + ".txt", "w")
                f_data.write(str(row_datas))

                delete_role_data_sql = 'delete from cbg_data where role_id in (select id from cbg_role where yn= 0)'
                delete_role_sql = 'delete from cbg_role where yn = 0'
                config.log_info(delete_role_data_sql)
                config.log_info(delete_role_sql)
                cursor.execute(delete_role_data_sql)
                cursor.execute(delete_role_sql)
            cursor.close()
            connection.commit()
        connection.close()

    def update_status(self):
        connection = pymysql.connect(**config.dbconfig)
        with connection.cursor() as cursor:
            update_sql = 'update cbg_role set yn = 0 where exp_time <=now()'
            config.log_info(update_sql)
            cursor.execute(update_sql)
            cursor.close()
        connection.commit()
        connection.close()

    def download_json(self, url):
        if url is None:
            return None
        headers = {'Content-Type': 'text/plain;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                   'Referer': 'http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search',
                   'Origin': 'http://tx3.cbg.163.com'}
        requests.adapters.DEFAULT_RETRIES = 3
        response = requests.get(url, headers=headers, timeout=3)
        config.log_info('craw:' + url)
        if response.status_code != 200:
            return None
        return response.text


def status_job():
    obj_spider = StatusSpider()
    config.log_error("status job start! time = " + str(datetime.datetime.now()))
    obj_spider.back_data()
    obj_spider.update_status()


if __name__ == "__main__":
    serverScheduler = BlockingScheduler()
    serverScheduler.add_job(status_job, 'interval', hours=1)
    serverScheduler.start()
