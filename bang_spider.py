# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import traceback
import configparser
import logging
import pymysql
import requests
import time
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


def get_urls():
    data = []
    connection = pymysql.connect(**dbconfig)
    try:
        with connection.cursor() as cursor:
            query = 'select url from bang_url'
            cursor.execute(query)
            res = cursor.fetchall()
            for r in res:
                data.append(r['url'])
            connection.commit()
    except Exception as ex:
        print(ex, traceback.print_exc())
        logging.exception(ex)
    finally:
        connection.close()
    return data


def get_data(url):
    data_array = []
    time.sleep(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }
    requests.adapters.DEFAULT_RETRIES = 3
    print('craw:' + url)
    res = requests.get(url, headers=headers, timeout=3)
    if res.status_code != 200:
        return data_array
    html_cont = res.content
    html = html_cont.decode("utf-8")
    tree = etree.HTML(html)

    tr1s = "//table/tr[@class='tr1']"
    trs = tree.xpath(tr1s)
    for tr in trs:
        index = 0
        data = {}
        for td in tr:
            if index == 1:
                childa = td.getchildren()
                data['name'] = childa[0].text
                data['role_id'] = childa[0].attrib['href'].split('/')[3]
            elif index == 2 and td.text is not None:
                data['area'] = td.text
            elif index == 3 and td.text is not None:
                data['server'] = td.text
            elif index == 4 and td.text is not None:
                data['level'] = td.text
            elif index == 5 and td.text is not None:
                data['school'] = td.text
            elif index == 6:
                childf = td.getchildren()
                if childf[0].text is not None:
                    data['family'] = childf[0].text
            elif index == 7 and td.text is not None:
                data['xiuwei'] = td.text
            elif index == 8 and td.text is not None:
                data['equ_xiuwei'] = td.text
            index += 1
        data_array.append(data)
    tr2s = "//table/tr[@class='tr2']"
    trs = tree.xpath(tr2s)
    for tr in trs:
        index = 0
        data = {}
        for td in tr:
            if index == 1:
                childa = td.getchildren()
                data['name'] = childa[0].text
                data['role_id'] = childa[0].attrib['href'].split('/')[3]
            elif index == 2 and td.text is not None:
                data['area'] = td.text
            elif index == 3 and td.text is not None:
                data['server'] = td.text
            elif index == 4 and td.text is not None:
                data['level'] = td.text
            elif index == 5 and td.text is not None:
                data['school'] = td.text
            elif index == 6:
                childf = td.getchildren()
                if childf[0].text is not None:
                    data['family'] = childf[0].text
            elif index == 7 and td.text is not None:
                data['xiuwei'] = td.text
            elif index == 8 and td.text is not None:
                data['equ_xiuwei'] = td.text
            index += 1
        data_array.append(data)
    return data_array


def add_mysql(datas):
    connection = pymysql.connect(**dbconfig)
    try:
        with connection.cursor() as cursor:
            for data in datas:
                query = 'select count(1) as count from bang_role where role_id = \'' + data['role_id'] + '\''
                cursor.execute(query)
                if cursor.fetchone()['count'] > 0:
                    continue
                sql = 'INSERT INTO bang_role (create_time'
                for key, value in data.items():
                    sql = sql + ',' + key
                sql += ' ) values ( now() '
                for key, value in data.items():
                    if type(value) == int:
                        sql = sql + ',' + value
                    else:
                        sql = sql + ',\'' + value + '\''
                sql += ')'
                logger.info(sql)
                cursor.execute(sql)
            connection.commit()
    except Exception as ex:
        print(ex, traceback.print_exc())
        logging.exception(ex)
    finally:
        connection.close()


urls = get_urls()
for url in urls:
    data_s = get_data(url)
    add_mysql(data_s)
