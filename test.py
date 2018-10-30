# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import configparser
import pymysql
import traceback
import datetime
import requests
import time
import json
import re

# fresh_time = '12月20日 10:23'
# mats = re.findall(r"\d+\.?\d*", fresh_time)
# print(mats)
#
# new_time = datetime.datetime(2016, int(mats[0]), int(mats[1]), int(mats[2]), int(mats[3]))
# print(new_time)



response = requests.get("http://tx3-ios2.spider.163.com/spider-center/query.py?&act=get_equip_detail&serverid=176&game_ordersn=e64d45b2-d5fa-11e8-9ebf-ecb1d7a5fc40")
json_data = json.loads(response.text)
print(json_data)