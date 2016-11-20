#!/usr/bin/python
#  -*- coding: utf-8 -*-
import pymysql.cursors
import traceback
import configparser

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


class Role(object):
    def addRoles(self, roles):
        connection = pymysql.connect(**dbconfig)
        try:
            with connection.cursor() as cursor:
                updatesql = 'update role set yn = 0 where exp_time <=now()'
                cursor.execute(updatesql)
                connection.commit()

                for role in roles:
                    query = 'select count(1) as count from role where role_id=' + str(role['role_id'])
                    cursor.execute(query)
                    if cursor.fetchone()['count'] > 0:
                        continue
                    sql = 'INSERT INTO role (yn,create_time'
                    for key, value in role.items():
                        sql = sql + ',' + key
                    sql += ' ) values (1,now()'
                    for key, value in role.items():
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
