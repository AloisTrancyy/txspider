# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job():
    print('hello world')


sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()