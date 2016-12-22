# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

from apscheduler.schedulers.blocking import BlockingScheduler
import configparser
import logging
import time
import bs4
import pymysql
import requests
import equ_spider
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


def get_data(role):
    data = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }
    url = 'http://bang.tx3.163.com/bang/role/' + role
    requests.adapters.DEFAULT_RETRIES = 3
    print(url)
    res = requests.get(url, headers=headers, timeout=3)
    if res.status_code != 200:
        return data
    html_cont = res.content
    soup = BeautifulSoup(html_cont, 'html.parser')
    data['role_id'] = role
    ################################################################
    s_level = soup.find('span', class_="sLev")
    a = 0
    for lc in s_level.children:
        if a == 1:
            data['level'] = lc.get_text()
        a += 1

    s_name = soup.find('span', class_="sTitle")
    data['name'] = s_name.get_text()

    s_exp = soup.find_all('span', class_="sExp")
    data['school'] = school_dict[s_exp[0].get_text()]
    aas = s_exp[1].children
    i = 0
    for aa in aas:
        if isinstance(aa, bs4.element.NavigableString):
            continue
        if i == 0:
            area_server = aa.get_text().split()
            data['area'] = area_server[0]
            data['server'] = area_server[1]
        else:
            data['family'] = aa.get_text()
        i += 1
    ###############################################################
    equ_xiuwei = soup.find_all('ul', class_="ulList_3")
    fly_soul_phase = ''
    fly_soul_lv = ''
    for equ in equ_xiuwei:
        for child in equ.children:
            if isinstance(child, bs4.element.NavigableString):
                continue
            equ_text = child.get_text()
            if '装备评价' in equ_text:
                data['equ_xiuwei'] = get_data_from_str(equ_text)
            elif '人物修为' in equ_text:
                data['xiuwei'] = get_data_from_str(equ_text)
            elif '神启阶段' in equ_text:
                fly_soul_phase = equ_text.split(':')[1]
            elif '神启境界' in equ_text:
                fly_soul_lv = equ_text.split(':')[1]

    data['level'] = get_level(data['level'], fly_soul_phase, fly_soul_lv)
    #####################################################################
    props = soup.find('div', class_="dEquips_1")
    index = 0
    for prop in props.children:
        if isinstance(prop, bs4.element.NavigableString):
            continue
        if index == 0:
            n = 0
            for li in prop.children:
                if isinstance(li, bs4.element.NavigableString):
                    continue
                if n == 1:
                    data['mhp'] = li.get_text()
                elif n == 3:
                    data['msp'] = li.get_text()
                elif n == 5:
                    data['strong'] = li.get_text()
                elif n == 7:
                    data['body'] = li.get_text()
                elif n == 9:
                    data['quich'] = li.get_text()
                elif n == 11:
                    data['dodge'] = li.get_text()
                elif n == 13:
                    data['soul'] = li.get_text()
                elif n == 15:
                    data['mind'] = li.get_text()
                n += 1
        elif index == 1:
            n = 0
            for li in prop.children:
                if isinstance(li, bs4.element.NavigableString):
                    continue
                if n == 1:
                    pats = re.findall(r"\d+\.?\d*", li.get_text())
                    data['pattack_min'] = pats[0]
                    data['pattack_max'] = pats[1]
                elif n == 2:
                    data['hit'] = get_data_from_str(li.get_text())
                elif n == 3:
                    mats = re.findall(r"\d+\.?\d*", li.get_text())
                    data['mattack_min'] = mats[0]
                    data['mattack_max'] = mats[1]
                elif n == 4:
                    data['modadd'] = get_data_from_str(li.get_text())
                elif n == 5:
                    data['critical'] = get_data_from_str(li.get_text())
                elif n == 6:
                    data['attadd'] = get_data_from_str(li.get_text())
                n += 1
        elif index == 2:
            n = 0
            for li in prop.children:
                if isinstance(li, bs4.element.NavigableString):
                    continue
                if n == 1:
                    data['pdef'] = get_data_from_str(li.get_text())
                elif n == 2:
                    data['avoid'] = get_data_from_str(li.get_text())
                elif n == 3:
                    data['mdef'] = get_data_from_str(li.get_text())
                elif n == 4:
                    data['inprotect'] = get_data_from_str(li.get_text())
                elif n == 5:
                    data['attdef'] = get_data_from_str(li.get_text())
                elif n == 6:
                    data['defhuman'] = get_data_from_str(li.get_text())
                n += 1
        elif index == 3:
            n = 0
            for li in prop.children:
                if isinstance(li, bs4.element.NavigableString):
                    continue
                if n == 1:
                    data['sract'] = get_data_from_str(li.get_text())
                elif n == 2:
                    data['srbody'] = get_data_from_str(li.get_text())
                elif n == 3:
                    data['srmind'] = get_data_from_str(li.get_text())
                elif n == 4:
                    data['cri_add_p'] = get_data_from_str(li.get_text())
                elif n == 5:
                    data['cri_sub_p'] = get_data_from_str(li.get_text())
                elif n == 6:
                    data['thump_add_p'] = get_data_from_str(li.get_text())
                elif n == 7:
                    data['thump_sub_p'] = get_data_from_str(li.get_text())
                n += 1
        elif index == 4:
            n = 0
            for li in prop.children:
                if isinstance(li, bs4.element.NavigableString):
                    continue
                if n == 1:
                    data['movespeed'] = get_data_from_str(li.get_text())
                elif n == 2:
                    data['attackspeed'] = get_data_from_str(li.get_text())
                elif n == 3:
                    data['castspeed'] = get_data_from_str(li.get_text())
                elif n == 6:
                    data['attackhuman'] = get_data_from_str(li.get_text())
                n += 1
        index += 1
    return data


def get_data_from_str(equ_text):
    sum_count = 0
    prop_value = re.findall(r"\d+\.?\d*", equ_text)
    for n in prop_value:
        if "." in n:
            sum_count += float(n)
        else:
            sum_count += int(n)
    return sum_count


def get_level(level, fly_soul_phase, fly_soul_lv):
    if fly_soul_phase is None or fly_soul_phase == '':
        return level
    if fly_soul_phase == '地魂':
        if '肆天玖境界' in fly_soul_lv:
            level = 85
        elif '肆天' in fly_soul_lv:
            level = 84
        elif '叁天' in fly_soul_lv:
            level = 83
        elif '贰天' in fly_soul_lv:
            level = 82
        elif '壹天' in fly_soul_lv:
            level = 81
    elif fly_soul_phase == '天魂':
        if '肆天玖境界' in fly_soul_lv:
            level = 90
        elif '肆天' in fly_soul_lv:
            level = 89
        elif '叁天' in fly_soul_lv:
            level = 88
        elif '贰天' in fly_soul_lv:
            level = 87
        elif '壹天' in fly_soul_lv:
            level = 86
    return level


def update_mysql(data):
    connection = pymysql.connect(**dbconfig)
    with connection.cursor() as cursor:
        data['craw'] = 1
        update_sql = 'update bang_role set '
        flag = 1
        for key, value in data.items():
            if flag == len(data):
                update_sql += key + '=\'' + str(value) + '\''
            else:
                update_sql += key + '=\'' + str(value) + '\','
            flag += 1
        update_sql += ' where role_id = \'' + str(data['role_id']) + '\''
        print(update_sql)
        cursor.execute(update_sql)
    connection.commit()
    connection.close()

def collect_role_data():
    logger.info("collect_role_data job start ")
    roles = equ_spider.get_roles()
    for role in roles:
        time.sleep(4)
        role_data = get_data(role)
        update_mysql(role_data)

if __name__ == '__main__':
    # serverScheduler = BlockingScheduler()
    # serverScheduler.add_job(collect_role_data, 'interval', hours=18)
    # serverScheduler.start()
    collect_role_data()