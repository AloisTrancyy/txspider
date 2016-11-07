#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : funny
# __create_time__ : 16/11/6 10:41

from bs4 import BeautifulSoup
import sys

class HtmlParser(object):
    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []
        res_data = {}
        try:
            soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
            tr1s = soup.find_all('tr', class_="tr1")
            for tr in tr1s:
                tds = tr.children
                for td in tds:
                    a = td.find('a')
                    if a is not None and a != -1:
                        res_data['url'] = a.get('href')
                        res_data['name'] = a.string
                data.append(res_data)

            tr2s = soup.find_all('tr', class_="tr2")
            for tr in tr2s:
                tds = tr.children
                for td in tds:
                    a = td.find('a')
                    if a is not None and a != -1:
                        res_data['url'] = a.get('href')
                        res_data['name'] = a.string
                data.append(res_data)

        except Exception as e:
            print 'parser error'
            print e

        print data
        return data
