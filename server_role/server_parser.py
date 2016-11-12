#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import json

class HtmlParser(object):
    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []
        json_data = json.loads(html_cont)
        msg = json_data['msg']
        for role in msg:
            res_data = {}
            res_data['equip_id'] = role['equipid']
            res_data['server_id'] = role['serverid']
            res_data['price'] = role['price']
            res_data['jiahu'] = role['jiahu']
            res_data['name'] = str(role['seller_nickname'].encode('utf-8').decode("utf-8"))
            res_data['url'] = "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail" \
                              "&equip_id="+str(role['equipid'])+"&serverid="+str(role['serverid'])
            data.append(res_data)
        return data
