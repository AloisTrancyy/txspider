#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : funny
# __create_time__ : 16/11/6 10:41

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []
        try:
            soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
            tr1s = soup.find_all('tr', class_="tr1")
            for tr in tr1s:
                res_data = {}
                tds = tr.children
                for index, td in enumerate(tds):
                    if index == 3:
                        a = td.find('a')
                        if a is not None and a != -1:
                            res_data['url'] = a.get('href')
                            res_data['name'] = td.string
                    elif index == 9:
                        res_data['level'] = td.string
                    elif index == 11:
                        res_data['school'] = td.string
                    elif index == 13:
                        res_data['family'] = td.string
                    elif index == 15:
                        res_data['xiuwei'] = td.string
                    elif index == 17:
                        res_data['eq'] = td.string

                data.append(res_data)

            tr2s = soup.find_all('tr', class_="tr2")
            for tr in tr2s:
                tds = tr.children
                res_data = {}
                for index, td in enumerate(tds):
                    if index == 3:
                        a = td.find('a')
                        if a is not None and a != -1:
                            res_data['url'] = a.get('href')
                            res_data['name'] = td.string
                    elif index == 9:
                        res_data['level'] = td.string
                    elif index == 11:
                        res_data['school'] = td.string
                    elif index == 13:
                        res_data['family'] = td.string
                    elif index == 15:
                        res_data['xiuwei'] = td.string
                    elif index == 17:
                        res_data['eq'] = td.string

                data.append(res_data)
        except Exception as e:
            print(e)
        return data
