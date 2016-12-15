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
    url = "http://bang.tx3.163.com/bang/role/" + url
    print(url)
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
        name = equ.get('name')
        if name is None:
            continue
        equ_type = equ.parent.find('span', class_='eq_type').text
        if equ_type != '通溟':
            data = {}
            data['equ_id'] = equ.parent.parent.parent.parent.find('img', class_='iImg')['src'].split('/')[6].split('.')[
                0]
            data['equ_name'] = equ.parent.find('h3').text
            data['equ_type'] = equ_type
        # props = get_values(equ['tx3text'])
        # data['prop'] = props
        data_array.append(data)
    return data_array


def add_mysql(datas):
    connection = pymysql.connect(**dbconfig)
    with connection.cursor() as cursor:
        for data in datas:
            insert_sql = 'insert into txs_equ (equ_id,equ_type,equ_name) VALUES ' \
                         '(\'' + str(data['equ_id']) + '\',\'' + data['equ_type'] + '\',\'' + data['equ_name'] + '\')'
            sql = "select count(1) as count from txs_equ where equ_id = \'" + str(data['equ_id']) + '\''
            cursor.execute(sql)
            res = cursor.fetchone()
            if res['count'] == 0:
                print(insert_sql)
                cursor.execute(insert_sql)
        cursor.close()
        connection.commit()
        connection.close()
    return


def get_props():
    data_s = []
    connection = pymysql.connect(**dbconfig)
    with connection.cursor() as cursor:
        sql = "select prop_name,prop_desc from property"
        cursor.execute(sql)
        res = cursor.fetchall()
        for prop in res:
            item = {}
            item[prop['prop_desc']] = prop['prop_name']
            data_s.append(item)
    connection.commit()
    connection.close()
    return data_s


def get_values(text):
    if text is None:
        return
    values = []
    props = get_props()
    for value in text.split('#'):
        if value is None or value == '':
            continue
        if value.isalpha():
            continue
        data = {}
        for prop in props:
            for desc, name in prop.items():
                if desc in value:
                    if desc == '魂' and '天魂' in value:
                        continue
                    if desc == '力' and ('定力' in value or '加成力' in value or '抵抗力' in value or '减伤力' in value):
                        continue
                    replaced = value.replace('cFF8800', '').replace('cBB44BB', '').replace('c7ecef4', '').replace(
                        'c8A00FF', '')
                    prop_value = re.findall(r"\d+\.?\d*", replaced)
                    sum_count = 0
                    for n in prop_value:
                        if "." in n:
                            sum_count += float(n)
                        else:
                            sum_count += int(n)
                    data[name] = sum_count
        if len(data) > 0:
            values.append(data)
    return values


def get_roles():
    data_s = []
    connection = pymysql.connect(**dbconfig)
    with connection.cursor() as cursor:
        for level in [69, 74, 79]:
            sql = 'select role_id from bang_role where level =' + str(level) + ' order by equ_xiuwei+xiuwei desc limit 2000'
            cursor.execute(sql)
            res = cursor.fetchall()
            for s in res:
                data_s.append(s['role_id'])

        sql = 'select role_id from bang_role where level >=80 order by equ_xiuwei+xiuwei desc limit 2000'
        cursor.execute(sql)
        res = cursor.fetchall()
        for s in res:
            data_s.append(s['role_id'])
    connection.commit()
    connection.close()
    return data_s


if __name__ == '__main__':
    urls = get_roles()
    for url in urls:
        role_data = get_data(url)
        add_mysql(role_data)
