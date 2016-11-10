# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import logging
import json
from bs4 import BeautifulSoup

# 设置logger
logger = logging.getLogger('test')
fHandler = logging.FileHandler('test.log')
logger.addHandler(fHandler)


class HtmlParser(object):
    def parse(self, html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(soup)
        return new_data

    def _get_new_data(self, soup):
        res_data = {}
        role_desc = soup.find('textarea', id="role_desc")
        role = role_desc.get_text()
        role_json = json.loads(role, 'utf-8')
        # 基础信息
        res_data['lv'] = role_json['lv']
        res_data['sch'] = role_json['sch']
        res_data['fly_soul_phase'] = role_json['fly_soul_phase']
        res_data['fly_soul_lv'] = role_json['fly_soul_lv']
        res_data['xiuwei'] = role_json['xiuwei']
        res_data['equ_xiuwei'] = role_json['equ_xiuwei']
        res_data['pattack_max'] = role_json['pattack_max']
        res_data['mattack_max'] = role_json['mattack_max']
        res_data['pattack_min'] = role_json['pattack_min']
        res_data['mattack_min'] = role_json['mattack_min']
        res_data['hit'] = role_json['critical']
        res_data['modadd'] = role_json['modadd']
        res_data['attadd'] = role_json['attadd']
        res_data['cri_add_p'] = role_json['cri_add_p']
        res_data['cri_sub_p'] = role_json['cri_sub_p']
        res_data['mdef'] = role_json['mdef']
        res_data['pdef'] = role_json['pdef']
        res_data['absolutely_attack'] = role_json['absolutely_attack']
        res_data['absolutely_defence'] = role_json['absolutely_defence']
        res_data['inprotect'] = role_json['inprotect']
        res_data['avoid'] = role_json['avoid']
        res_data['attdef'] = role_json['attdef']
        res_data['defhuman'] = role_json['defhuman']
        res_data['attackhuman'] = role_json['attackhuman']
        res_data['sract'] = role_json['sract']
        res_data['srbody'] = role_json['srbody']
        res_data['srmind'] = role_json['srmind']
        res_data['movespeed'] = role_json['movespeed']
        res_data['castspeed'] = role_json['castspeed']
        res_data['attackspeed'] = role_json['attackspeed']
        res_data['thump_add_p'] = role_json['thump_add_p']
        res_data['thump_sub_p'] = role_json['thump_sub_p']
        res_data['str'] = role_json['str']
        res_data['con'] = role_json['con']
        res_data['dex'] = role_json['dex']
        res_data['dog'] = role_json['dog']
        res_data['int'] = role_json['int']
        res_data['mind'] = role_json['mind']

        res_data['cash'] = role_json['cash']
        # 轻功
        lingskills = role_json['lightSkills']

        # 门派轻功
        school_qinggong = role_json['school_qinggong']

        # 声望
        credit = role_json['credit']

        # 觉醒
        final_skill = role_json['final_skill']

        # 英魂
        lingskills = role_json['multiMS']

        # 元魂珠
        lingskills = role_json['monster_souls']

        # 灵兽
        hbs = role_json['hbs']

        # 孩子
        childs = role_json['new_childs']
        for child in childs:
            # 资质
            potential = child['potential']
            # 统帅
            commander = child['commander']
            # 学识
            knowledge = child['knowledge']
            # 武学
            kongfu = child['kongfu']
            # 等级
            lv = child['lv']

            # 武器
            equs = child['equs']
            if equs is None or len(equs) == 0 :
                continue
            for key, value in equs.items():
                # 武器
                if key == 0 :
                    print value
                # 帽子
                elif key == 1 :
                    print value
                # 衣服
                elif key == 2:
                    print value
                # 裤子
                elif key == 3:
                    print value
                # 鞋子
                elif key == 4:
                    print value
                # 项链
                elif key == 5:
                    print value

        # 时装
        formated_role_desc = soup.find('textarea', id="formated_role_desc")
        format_role = formated_role_desc.get_text()
        format_role_json = json.loads(format_role, 'utf-8')
        for key, value in format_role_json['clothes_info'].items():
            print key, value['name']
        return res_data
