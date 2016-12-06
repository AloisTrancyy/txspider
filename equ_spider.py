# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import traceback
import configparser
import logging
import pymysql
import requests
import time
import re
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='spider.log',
                    filemode='w')
logger = logging.getLogger('bang_spider')

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


def get_data(url):
    data_array = []
    time.sleep(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }
    requests.adapters.DEFAULT_RETRIES = 3
    res = requests.get(url, headers=headers, timeout=3)
    if res.status_code != 200:
        return data_array
    html_cont = res.content
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
    equs = soup.find_all('div', class_='tx3TextBlock')
    for equ in equs:
        data = {}
        name = equ.get('name')
        if name is None:
            continue
        data['equ_name'] = equ.parent.find('h3').text
        equ_type = equ.parent.find('span', class_='eq_type').text
        data['equ_type'] = equ_type
        if equ_type != '通溟':
            data['equ_id'] = equ.parent.parent.parent.parent.find('img', class_='iImg')['src'].split('/')[6].split('.')[
                0]
        print(data)
    return data_array


def add_mysql(datas):
    if datas is None or len(datas) == 0:
        return
    connection = pymysql.connect(**dbconfig)
    try:
        with connection.cursor() as cursor:

            connection.commit()
    except Exception as ex:
        print(ex, traceback.print_exc())
        logging.exception(ex)
    finally:
        connection.close()


url = "http://bang.tx3.163.com/bang/role/32_57551"
data_s = get_data(url)
add_mysql(data_s)
