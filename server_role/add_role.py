#!/usr/bin/python
#  -*- coding: utf-8 -*-
import pymysql.cursors
import traceback

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'spider',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

class Role(object):
    def addRoles(self, roles):
        connection = pymysql.connect(**config)
        try:
            with connection.cursor() as cursor:
                for role in roles:
                    sql = 'INSERT INTO role (equip_id'
                    for key, value in role.items():
                        if key == 'equip_id':
                            continue
                        sql = sql + ',' + key
                    sql = sql + ' ) values (' + str(role['equip_id'])
                    for key, value in role.items():
                        if key == 'equip_id':
                            continue
                        if type(value) == int:
                            sql = sql + ',' + str(value)
                        else:
                            sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''

                    sql += ')'
                    print(sql)
                    cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e, traceback.print_exc())
        finally:
            connection.close()