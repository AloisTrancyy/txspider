# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
