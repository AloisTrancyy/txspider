# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = requests.get(url, )
        if response.status_code != 200:
            return None
        response.encoding = 'utf-8'  # 显式地指定网页编码，一般情况可以不用
        return response.content
