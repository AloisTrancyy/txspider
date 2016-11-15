# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import configparser
import datetime
import time

config = configparser.ConfigParser()
config.read("config.ini")

if __name__ == '__main__':
    day, hour, minute = 0, 0, 0
    exp_time = '6天1小时33分钟'
    if '天' in exp_time:
        day = exp_time[0:exp_time.index("天")]
        hour = exp_time[exp_time.index("天") + 1:exp_time.index('小时')]
        minute = exp_time[exp_time.index("小时") + 2:exp_time.index('分钟')]
    else:
        if '小时' in exp_time:
            hour = exp_time[0:exp_time.index('小时')]
            minute = exp_time[exp_time.index("小时") + 2:exp_time.index('分钟')]

    print(day, hour, minute)
    now = datetime.datetime.now()
    date = now + datetime.timedelta(days=int(day)) + datetime.timedelta(hours=int(hour)) + datetime.timedelta(
        minutes=int(minute))

    print(date.strftime('%Y-%m-%d %H:%M:%S'))
