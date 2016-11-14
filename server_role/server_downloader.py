# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import requests


class HtmlDownloader(object):
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
