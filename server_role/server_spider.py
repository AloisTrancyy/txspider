# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import server_url_manager
import server_downloader
import server_parser
import add_role

class ServerSpider(object):
    def __init__(self):
        self.urls = server_url_manager.UrlManager()
        self.downloader = server_downloader.HtmlDownloader()
        self.parser = server_parser.HtmlParser()
        self.store = add_role.Role()

    def craw(self):
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw :' + new_url
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse(html_cont)
                self.store.addRoles(new_data)
            except Exception as e:
                print e

servers = ['东方明珠',
           '紫禁之巅',
           '君临天下',
           '天生王者',
           '幻龙诀',
           '气壮山河',
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
           '齐鲁天下'
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
           '盛世长安']

if __name__ == "__main__":
    obj_spider = ServerSpider()
    for server_name in servers:
        url = "http://bang.tx3.163.com/bang/ranks?server=" + server_name
        obj_spider.urls.add_new_url(url)

    obj_spider.craw()
