# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
from apscheduler.schedulers.blocking import BlockingScheduler
from cbg_data_spider import data_job, data_test
from cbg_role_spider import role_job, role_test

serverScheduler = BlockingScheduler()
# serverScheduler.add_job(data_test, trigger='cron', minute='*/30',hour='*/1')
# serverScheduler.add_job(role_test, trigger='cron', minute='*/20',hour='*/1')

serverScheduler.add_job(data_job, trigger='cron', minute='*/20',hour='*/1')
serverScheduler.add_job(role_job, trigger='cron', minute='*/30',hour='*/1')
serverScheduler.start()
