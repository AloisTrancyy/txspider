# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import configparser
import pymysql
import traceback
import datetime
import time
import json
import re

fresh_time = '12月20日 10:23'
mats = re.findall(r"\d+\.?\d*", fresh_time)
print(mats)

new_time = datetime.datetime(2016, int(mats[0]), int(mats[1]), int(mats[2]), int(mats[3]))
print(new_time)
