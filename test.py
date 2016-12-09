# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import configparser
import pymysql
import traceback
import datetime
import time
import json

config = configparser.ConfigParser()
config.read("config.ini")
dbconfig = {
    'host': config.get('mysql', 'host'),
    'port': config.getint('mysql', 'port'),
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'db': config.get('mysql', 'db'),
    'charset': config.get('mysql', 'charset'),
    'cursorclass': pymysql.cursors.DictCursor
}
print(type(time.strftime('%Y-%m-%d',time.localtime(time.time()))))