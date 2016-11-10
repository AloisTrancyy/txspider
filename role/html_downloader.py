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
        return response.content
