#!/usr/bin/python
#  -*- coding: utf-8 -*-
import pymysql.cursors

config = {
    'host': '10.168.66.173',
    'port': 3306,
    'user': 'sellmall',
    'password': 'sellmall1234',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

school = {
        '荒火教'.decode("utf-8"): 1,
        '天机营'.decode("utf-8"): 2,
        '翎羽山庄'.decode("utf-8"): 3,
        '魍魉'.decode("utf-8"): 4,
        '太虚观'.decode("utf-8"): 5,
        '云麓仙居'.decode("utf-8"): 6,
        '冰心堂'.decode("utf-8"): 7,
        '弈剑听雨阁'.decode("utf-8"): 8,
        '鬼墨'.decode("utf-8"): 9,
        '龙巫宫'.decode("utf-8"): 10,
        '幽篁国'.decode("utf-8"): 11
}


class Role(object):
    def addRoles(self, roles):
        connection = pymysql.connect(**config)
        try:
            for role in roles:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO role (role_id,role_name,role_url,role_school,role_level,role_family,' \
                          ' role_xiuwei,role_eq) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                    role['id'] = role['url'].replace('/bang/role/', '')
                    role_school = school[role['school']]
                    cursor.execute(sql, (role['id'], role['name'], role['url'], role_school,
                                         role['level'], role['family'], role['xiuwei'], role['eq']))
            connection.commit()
        except Exception as e:
            print e
        finally:
            connection.close()