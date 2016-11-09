# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
# URL调度器


class UrlManager(object):
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    def add_new_url(self, url):
        if url not in self.new_url and url not in self.old_url:
            page_number = 1
            while page_number <= 25:
                page_url = url+'&page=' + str(page_number)
                print page_url
                self.new_url.add(page_url)
                page_number += 1

    def has_new_url(self):
        return len(self.new_url) != 0

    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url
