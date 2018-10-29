# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import traceback
import logging
import pymysql
import requests
import time
import lxml.etree as etree
from profile import config

school_dict = {
    '荒火教': 1,
    '天机营': 2,
    '翎羽山庄': 3,
    '魍魉': 4,
    '太虚观': 5,
    '云麓仙居': 6,
    '冰心堂': 7,
    '弈剑听雨阁': 8,
    '鬼墨': 9,
    '龙巫宫': 10,
    '幽篁国': 11,
}

def get_urls():
    connection = pymysql.connect(**config.dbconfig)
    try:
        with connection.cursor() as cursor:
            query = 'select id,url from bang_url where craw = 0 '
            cursor.execute(query)
            res = cursor.fetchall()
            connection.commit()
    except Exception as ex:
        print(ex, traceback.print_exc())
        logging.exception(ex)
    finally:
        connection.close()
    return res


def get_data(info):
    data_array = []
    time.sleep(3)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }
    url = info['url']
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
                data['school'] = school_dict[td.text]
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
                data['school'] = school_dict[td.text]
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
    return data_array, info['id']


def add_mysql(datas, id):
    connection = pymysql.connect(**config.dbconfig)
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
                        sql = sql + ',' + str(value)
                    else:
                        sql = sql + ',\'' + value + '\''
                sql += ')'
                cursor.execute(sql)
                print(sql)
            update_sql = 'update bang_url set craw = 1 where id = ' + str(id)
            cursor.execute(update_sql)
            connection.commit()
    except Exception as ex:
        print(ex, traceback.print_exc())
        logging.exception(ex)
    finally:
        connection.close()


urls = get_urls()
for url in urls:
    data_s, id = get_data(url)
    add_mysql(data_s, id)
