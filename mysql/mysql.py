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


class Role(object):
    def __int__(self, role_id, role_name, role_url):
        self.role_id = role_id
        self.role_name = role_name
        self.role_url = role_url

    def addRole(self, connection):
        connection = self.getConnection();
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO role (role_id,role_name,role_url) VALUES (%s,%s,%s)'
                cursor.execute(sql, (self.role_id, self.role_name, self.role_url))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        except Exception, e:
            print(str(e))
        finally:
            connection.close()

    def addRoles(self, roles):
        for role in roles:
            connection = self.getConnection();
            self.addRole(connection)

    def getConnection(self):
        connection = pymysql.connect(**config)
        return connection
