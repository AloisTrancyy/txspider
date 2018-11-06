# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import time
import datetime
import requests
import json
import pymysql
import config
from apscheduler.schedulers.blocking import BlockingScheduler

from logger import Logger


class ServerSpider(object):
    log = Logger('role.log', level='info')
    def craw(self):
        res = []
        connection = pymysql.connect(**config.dbconfig)
        with connection.cursor() as cursor:
            delete_sql = "delete from cbg_role where yn = 0 "
            self.log.logger.info(delete_sql)
            cursor.execute(delete_sql)

            sql = "select url from cbg_url order by id desc "
            self.log.logger.info(sql)
            cursor.execute(sql)

            res = cursor.fetchall()
        connection.close()
        for url in res:
            time.sleep(3)
            try:
                html_cont = self.download(url['url'])
                new_data = self.parse(html_cont)
                self.add_role(new_data)
            except Exception as e:
                pass
                self.log.logger.exception(e)


    def add_role(self, roles):
        if roles is None or len(roles) == 0:
            return
        try:
            connection = pymysql.connect(**config.dbconfig)
            with connection.cursor() as cursor:
                for role in roles:
                    query = 'select count(1) as count from cbg_role where yn=1 and role_key=\'' + str(
                        role['role_key']) + ' \' and server_id=' + str(role['server_id'])
                    cursor.execute(query)
                    if cursor.fetchone()['count'] == 0:
                        sql = 'INSERT INTO cbg_role (yn,create_time'
                        for key, value in role.items():
                            sql = sql + ',' + key
                        sql += ' ) values (1,now()'
                        for key, value in role.items():
                            if type(value) == int:
                                sql = sql + ',' + str(value)
                            else:
                                sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''
                        sql += ')'
                        self.log.logger.info(sql)
                        cursor.execute(sql)
                connection.commit()
        except Exception as e:
            print(e)
            pass
        finally:
            connection.close()

    def download(self, url):
        if url is None:
            return None
        headers = {'Content-Type': 'text/plain;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                   'Referer': 'http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search',
                   'Origin': 'http://tx3.cbg.163.com'}
        requests.adapters.DEFAULT_RETRIES = 3
        response = requests.get(url, headers=headers, timeout=3)
        self.log.logger.info('craw:'+url)
        if response.status_code != 200:
            return None
        return response.text

    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []
        json_data = json.loads(html_cont)
        equip_list = json_data['equip_list']
        if equip_list is None or len(equip_list) == 0:
            return
        for role in equip_list:
            res_data = {}
            res_data['role_key'] = role['game_ordersn']
            res_data['server_id'] = role['equip_serverid']
            res_data['price'] = role['price_desc'].replace('￥', '')
            res_data['jiahu'] = role['subtitle'].split("加护")[1]
            nickname = str(role['equip_name'].encode('utf-8').decode("utf-8"))
            if '@' in nickname:
                nickname = nickname[0:nickname.find('@')]
            res_data['name'] = nickname
            res_data['data_url'] = 'http://tx3-ios2.cbg.163.com/cbg-center/query.py?&act=get_equip_detail&' \
                                   'serverid=' + str(res_data['server_id']) + '&game_ordersn=' + res_data['role_key']
            res_data['url'] = 'http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=buy_show_by_ordersn&' \
                              'server_id=' + str(res_data['server_id']) + '&ordersn=' + res_data['role_key']
            data.append(res_data)
        return data

def server_job():
    obj_spider = ServerSpider()
    obj_spider.craw()


if __name__ == "__main__":
    serverScheduler = BlockingScheduler()
    serverScheduler.add_job(server_job, 'interval', hours=2)
    serverScheduler.start()
    # server_job()
