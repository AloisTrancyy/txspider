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
    res_url = set()
    connection = pymysql.connect(**dbconfig)
    try:
        with connection.cursor() as cursor:
            query = 'select t.id,t.detail_url from car_resource t where t.res_type=1 and craw = 0'
            cursor.execute(query)
            res_url = cursor.fetchall()
    except Exception as ex:
        print(traceback.print_exc(ex))
        logging.exception(ex)
    finally:
        connection.close()
    return res_url


def get_data(res):
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
    url = 'http://www.chehang168.com' + res['detail_url']
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
        data['res_id'] = res['id']
        td_index = 1
        for td in tr:
            if td_index == 2 and td.text is not None:
                data['brand_name'] = td.text
            elif td_index == 3 and td.text is not None:
                data['spec_name'] = td.text
            elif td_index == 4 and td.text is not None:
                data['color'] = td.text
            elif td_index == 5 and td.text is not None:
                data['config'] = td.text
            elif td_index == 6 and td.text is not None:
                data['price'] = td.text
            elif td_index == 7 and td.text is not None:
                data['status'] = td.text
            elif td_index == 8 and td.text is not None:
                data['sale_area'] = td.text
            elif td_index == 9 and td.text is not None:
                data['note'] = td.text
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
                # sql = 'INSERT INTO car_resource_detail (create_time'
                # for key, value in data.items():
                #     sql = sql + ',' + key
                # sql += ' ) values ( now() '
                # for key, value in data.items():
                #     if type(value) == int:
                #         sql = sql + ',' + value
                #     else:
                #         sql = sql + ',\'' + value + '\''
                # sql += ')'
                # print(sql)
                # cursor.execute(sql)
            connection.commit()
    except Exception as ex:
        print(traceback.print_exc(ex))
        logging.exception(ex)
    finally:
        connection.close()


res_list = get_urls()
while len(res_list) != 0:
    res = res_list.pop()
    data_list = get_data(res)
    add_mysql(data_list)