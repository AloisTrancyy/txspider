# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import configparser
import logging
import pymysql
import traceback

profile_config = configparser.ConfigParser()
profile_config.read('../profile/test.ini')

dbconfig = {
    'host': profile_config.get('mysql', 'host'),
    'port': profile_config.getint('mysql', 'port'),
    'user': profile_config.get('mysql', 'user'),
    'password': profile_config.get('mysql', 'password'),
    'db': profile_config.get('mysql', 'db'),
    'charset': profile_config.get('mysql', 'charset'),
    'cursorclass': pymysql.cursors.DictCursor
}
show_sql = profile_config.getboolean('mysql', 'show_sql')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='info.log',
                    filemode='w')
info_logger = logging.getLogger('info_logger')

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='error.log',
                    filemode='w')
error_logger = logging.getLogger('error_logger')

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='exception.log',
                    filemode='w')
exception_logger = logging.getLogger('exception_logger')


def log_info(text):
    if show_sql:
        print(text)
        #info_logger.info(text)


def log_error(text):
    error_logger.error(text)


def log_exception(text):
    traceback.print_exc(text)
    exception_logger.exception(text)
    error_logger.error(text)
