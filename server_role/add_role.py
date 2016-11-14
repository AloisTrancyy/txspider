#!/usr/bin/python
#  -*- coding: utf-8 -*-
import pymysql.cursors
import traceback
import config


class Role(object):
    def addRoles(self, roles):
        try:
            connection = pymysql.connect(host=config.get('mysql', 'host'),
                                         port=config.get('mysql', 'port'),
                                         user=config.get('mysql', 'user'),
                                         password=config.get('mysql', 'password'),
                                         db=config.get('mysql', 'db'),
                                         charset=config.get('mysql', 'charset'),
                                         cursorclass=config.get('mysql', 'cursorclass'))
            with connection.cursor() as cursor:
                for role in roles:
                    query = 'select count(1) as count from role where equip_id=' + str(role['equip_id'])
                    cursor.execute(query)
                    if cursor.fetchone()['count'] > 0:
                        continue
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
