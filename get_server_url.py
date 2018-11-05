# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import pymysql
import config


class URLSpider(object):
    def get_url_array(self):
        array = []
        # 69战场
        for school in range(10):
            url = 'http://tx3-ios2.cbg.163.com/cbg-center/search.py?num_per_page=15&products=tx2&' \
                  'act=basic_search_role&order_refer=8&price_min=50000&price_max=29999900&level_min=69&level_max=69'
            url += "&school=" + str(school + 1)
            for page in range(10):
                page_url = "&page=" + str(page + 1)
                array.append(url + page_url)
        # 74战场
        for school in range(10):
            url = 'http://tx3-ios2.cbg.163.com/cbg-center/search.py?num_per_page=15&products=tx2&' \
                  'act=basic_search_role&order_refer=8&price_min=50000&price_max=29999900&level_min=70&level_max=74'
            url += "&school=" + str(school + 1)
            for page in range(10):
                page_url = "&page=" + str(page + 1)
                array.append(url + page_url)
        # 79战场
        for school in range(10):
            url = 'http://tx3-ios2.cbg.163.com/cbg-center/search.py?num_per_page=15&products=tx2&' \
                  'act=basic_search_role&order_refer=8&price_min=50000&price_max=29999900&level_min=75&level_max=79'
            url += "&school=" + str(school + 1)
            for page in range(10):
                page_url = "&page=" + str(page + 1)
                array.append(url + page_url)
        # 神启
        for school in range(11):
            url = 'http://tx3-ios2.cbg.163.com/cbg-center/search.py?num_per_page=15&products=tx2&' \
                  'act=basic_search_role&order_refer=8&price_min=50000&price_max=29999900&level_min=80&level_max=80'
            url += "&school=" + str(school + 1)
            for page in range(10):
                page_url = "&page=" + str(page + 1)
                array.append(url + page_url)
        return array

    def add_url(self, url_array):
        connection = pymysql.connect(**config.dbconfig)
        with connection.cursor() as cursor:
            for url in url_array:
                sql = 'insert into cbg_url(url) values(\'' + url + '\')'
                cursor.execute(sql)
            cursor.close()
        connection.commit()
        connection.close()

if __name__ == "__main__":
    url_spider = URLSpider()
    url_array = url_spider.get_url_array()
    url_spider.add_url(url_array)
