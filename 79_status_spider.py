# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import datetime
import pymysql
from profile import config
from apscheduler.schedulers.blocking import BlockingScheduler


class StatusSpider(object):
    def update_status(self):
        connection = pymysql.connect(**config.dbconfig)
        with connection.cursor() as cursor:
            update_sql = 'update bang_role t set t.craw=0 where t.level=79'
            config.log_info(update_sql)
            cursor.execute(update_sql)
            cursor.close()
        connection.commit()
        connection.close()


def status_job():
    obj_spider = StatusSpider()
    config.log_error("update 79 status job start! time = " + str(datetime.datetime.now()))
    obj_spider.back_data()
    obj_spider.update_status()


if __name__ == "__main__":
    serverScheduler = BlockingScheduler()
    serverScheduler.add_job(status_job, 'interval', days=3)
    serverScheduler.start()
