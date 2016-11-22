# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import traceback
import logging
import time
import datetime
import requests
import json
import pymysql
import configparser

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='spider.log',
                    filemode='w')
logger = logging.getLogger('server_spider')
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


class ServerSpider(object):
    new_url = set()
    old_url = set()

    def craw(self):
        while self.has_new_url():
            time.sleep(10)
            try:
                new_url = self.get_new_url()
                print('craw :' + new_url)
                logger.info('craw :' + new_url)
                html_cont = self.download(new_url)
                new_data = self.parse(html_cont)
                self.add_role(new_data)
            except Exception as e:
                print(e, traceback.print_exc())
                logger.exception(e)

    def add_role(self, roles):
        try:
            connection = pymysql.connect(**dbconfig)
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
                    logger.info(sql)
                    cursor.execute(sql)
            connection.commit()
        except Exception as e:
            raise Exception(e)
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
        if response.status_code != 200:
            return None
        return response.text

    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []
        json_data = json.loads(html_cont)
        msg = json_data['msg']
        for role in msg:
            res_data = {}
            res_data['role_id'] = role['equipid']
            res_data['server_id'] = role['serverid']
            res_data['price'] = role['price']
            res_data['jiahu'] = role['jiahu']
            nickname = str(role['seller_nickname'].encode('utf-8').decode("utf-8"))
            if '@' in nickname:
                nickname = nickname[0:nickname.find('@')]

            res_data['name'] = nickname
            res_data['url'] = "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail" \
                              "&equip_id=" + str(role['equipid']) + "&serverid=" + str(role['serverid'])

            res_data['exp_time'] = self.get_exp_time(role['expire_time'])
            data.append(res_data)
        return data

    def get_exp_time(self, exp_time):
        day, hour, minute = 0, 0, 0
        if '天' in exp_time:
            day = exp_time[0:exp_time.index("天")]
            hour = exp_time[exp_time.index("天") + 1:exp_time.index('小时')]
            minute = exp_time[exp_time.index("小时") + 2:exp_time.index('分钟')]
        else:
            if '小时' in exp_time:
                hour = exp_time[0:exp_time.index('小时')]
                minute = exp_time[exp_time.index("小时") + 2:exp_time.index('分钟')]
        now = datetime.datetime.now()
        date = now + datetime.timedelta(days=int(day)) + datetime.timedelta(hours=int(hour)) + datetime.timedelta(
            minutes=int(minute))
        return date.strftime('%Y-%m-%d %H:%M:%S')

    def add_new_url(self, url):
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    def has_new_url(self):
        return len(self.new_url) != 0

    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url