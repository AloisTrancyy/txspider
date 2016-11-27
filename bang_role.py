# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import time
import traceback
import configparser
import logging
import pymysql
import json
import datetime
import requests
import lxml.etree as etree
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
from server_spider import ServerSpider

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
servers = [
    '东方明珠',
    '君临天下',
    '天生王者',
    '幻龙诀',
    '气壮山河',
    '紫禁之巅',
    '天府之国',
    '墨倾天下',
    '碧海青天',
    '笑看风云',
    '逍遥三界',
    '魔影幽篁',
    '万里惊涛',
    '剑啸苍穹',
    '剑指山河',
    '天下无双',
    '天外飞仙',
    '忘忧海',
    '情动大荒',
    '枫丹白露',
    '烟花三月',
    '琉璃月',
    '纵横四海',
    '致青春',
    '醉红尘',
    '齐鲁天下',
    '剑舞香江',
    '白云山',
    '瘦西湖',
    '逐鹿中原',
    '三潭印月',
    '烟雨江南',
    '黄鹤楼',
    '洞庭湖',
    '弱水三千',
    '武夷九曲',
    '上善若水',
    '飞龙在天',
    '烽火关东',
    '盛世长安'
]

urls = []
for server in servers:
    for page in range(26):
        url = 'http://bang.tx3.163.com/bang/ranks?order_key=total_xiuwei&server=' + server + '&page=' + str(
            page + 1)
        urls.append(url)

url = 'http://bang.tx3.163.com/bang/ranks?order_key=total_xiuwei&server=%E4%B8%9C%E6%96%B9%E6%98%8E%E7%8F%A0&page=1'

res = requests.get(url)
if res.status_code == 200:
    html_cont = res.content
    html = html_cont.decode("utf-8")
    tree = etree.HTML(html)
    property_list_reg = "//table/tr//td/text()"
    property_lst = tree.xpath(property_list_reg)
    print(property_lst)
