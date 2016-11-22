#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import json
import datetime


class HtmlParser(object):
    def parse(self, html_cont):
        if html_cont is None:
            return
        data = []
        json_data = json.loads(html_cont)
        msg = json_data['msg']
        for role in msg:
            res_data = {}
            res_data['role_id'] = role['equipid']
            res_data['server_id'] = role['serverid']
            res_data['price'] = role['price']
            res_data['jiahu'] = role['jiahu']
            ## 乄风清灬@西江月@F69990F50B0211DEAA93001EC9B892ED
            nickname = str(role['seller_nickname'].encode('utf-8').decode("utf-8"))
            if '@' in nickname:
                nickname = nickname[0:nickname.find('@')]

            res_data['name'] = nickname
            res_data['url'] = "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail" \
                              "&equip_id=" + str(role['equipid']) + "&serverid=" + str(role['serverid'])

            res_data['exp_time'] = self.getExpTime(role['expire_time'])
            data.append(res_data)
        return data

    def getExpTime(self, exp_time):
        day, hour, minute = 0, 0, 0
        if '天' in exp_time:
            day = exp_time[0:exp_time.index("天")]
            hour = exp_time[exp_time.index("天") + 1:exp_time.index('小时')]
            minute = exp_time[exp_time.index("小时") + 2:exp_time.index('分钟')]
        else:
            if '小时' in exp_time:
                hour = exp_time[0:exp_time.index('小时')]
                minute = exp_time[exp_time.index("小时") + 2:exp_time.index('分钟')]
        now = datetime.datetime.now()
        date = now + datetime.timedelta(days=int(day)) + datetime.timedelta(hours=int(hour)) + datetime.timedelta(
            minutes=int(minute))
        return date.strftime('%Y-%m-%d %H:%M:%S')
