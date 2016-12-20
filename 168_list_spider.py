# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import traceback
import configparser
import logging
import pymysql
import requests
import time
import datetime
import re
import lxml.etree as etree

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


def get_urls():
    res_url = []
    for page in range(2):
        res_url.append('http://www.chehang168.com/index.php?c=index&m=zyList&page=' + str(page + 1))
        res_url.append('http://www.chehang168.com/index.php?c=index&m=zyList&type=1&page=' + str(page + 1))
    return res_url


def get_data(url):
    data_array = []
    time.sleep(2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }
    cookies = {
        'U': '238728_9474a5c2a50741e81507131654e6e3a5',
        'SERVERID': '5453c49dad5b9c491daed5aecccecb9e|1482197769|1482196311'
    }
    requests.adapters.DEFAULT_RETRIES = 3
    print('craw:' + url)
    res = requests.get(url, headers=headers, timeout=3, cookies=cookies)
    if res.status_code != 200:
        return data_array
    html_cont = res.content
    html = html_cont.decode("utf-8")
    tree = etree.HTML(html)
    trs = tree.xpath("//table/tbody/tr")
    tr_index = 1
    for tr in trs:
        if tr_index == 1:
            tr_index += 1
            continue
        data = {}
        td_index = 1
        for td in tr:
            if td_index == 1:
                childa = td.getchildren()
                data['res_name'] = childa[0].text
                detail_url = childa[0].attrib['href']
                data['detail_url'] = detail_url
                for param in detail_url.split('&'):
                    if 'uid' in param:
                        data['uid'] = param.split('=')[1]
            elif td_index == 2 and td.text is not None:
                data['city_name'] = td.text
            elif td_index == 4 and td.text is not None:
                mats = re.findall(r"\d+\.?\d*", td.text)
                data['fresh_time'] = str(datetime.datetime(2016, int(mats[0]), int(mats[1]), int(mats[2]), int(mats[3])))
            td_index += 1
        tr_index += 1
        data_array.append(data)
    return data_array


def add_mysql(datas):
    connection = pymysql.connect(**dbconfig)
    try:
        with connection.cursor() as cursor:
            for data in datas:
                print(data)
                query = 'select count(1) as count from car_resource where uid = \'' + data['uid'] + '\''
                print(query)
                cursor.execute(query)
                if cursor.fetchone()['count'] > 0:
                    continue
                sql = 'INSERT INTO car_resource (create_time'
                for key, value in data.items():
                    sql = sql + ',' + key
                sql += ' ) values ( now() '
                for key, value in data.items():
                    if type(value) == int:
                        sql = sql + ',' + value
                    else:
                        sql = sql + ',\'' + value + '\''
                sql += ')'
                print(sql)
                cursor.execute(sql)
            connection.commit()
    except Exception as ex:
        print(traceback.print_exc(ex))
        logging.exception(ex)
    finally:
        connection.close()


urls = get_urls()
for url in urls:
    time.sleep(2)
    data_s = get_data(url)
    add_mysql(data_s)
