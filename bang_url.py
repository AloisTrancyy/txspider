# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 2016/12/6 13:45

import traceback
import pymysql

import config

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
    '盛世长安',
    '众星捧月',
    '飞鸿踏雪',
    '昆仑变',
    '踏歌山海',
    '剑啸昆仑',
    '暮雪轻歌',
    '云里江南',
]

urls = []
for server in servers:
    for page in range(25):
        for school in range(11):
            url = 'http://bang.tx3.163.com/bang/ranks?order_key=equ_xiuwei&school=' + str(
                school + 1) + '&server=' + server + '&page=' + str(page + 1)
            urls.append(url)

for server in servers:
    for page in range(25):
        for school in range(11):
            url = 'http://bang.tx3.163.com/bang/ranks?order_key=xiuwei&school=' + str(
                school + 1) + '&server=' + server + '&page=' + str(page + 1)
            urls.append(url)

connection = pymysql.connect(**config.dbconfig)
try:
    with connection.cursor() as cursor:
        for data in urls:
            sql = 'INSERT INTO bang_url(url) values (\'' + data + '\')'
            print(sql)
            cursor.execute(sql)
        connection.commit()
except Exception as ex:
    print(ex, traceback.print_exc())
finally:
    connection.close()
