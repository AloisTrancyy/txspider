# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

print(config.get('mysql', 'host'))
