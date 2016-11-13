# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import json
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, html_cont, equip_id):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(soup, equip_id)
        return new_data

    def _get_new_data(self, soup, equip_id):
        res_data = {}
        calc_data = {}
        res_data['role_id'] = equip_id
        calc_data['role_id'] = equip_id

        role_desc = soup.find('textarea', id="role_desc")
        role = role_desc.get_text()
        role_json = json.loads(role, 'utf-8')

        # 基础信息
        res_data['lv'] = role_json['lv']
        role_json.setdefault('fly_soul_phase', None)
        role_json.setdefault('fly_soul_lv', None)
        res_data['fly_soul_phase'] = role_json['fly_soul_phase']
        res_data['fly_soul_lv'] = role_json['fly_soul_lv']
        res_data['xiuwei'] = role_json['xiuwei']
        res_data['equ_xiuwei'] = role_json['equ_xiuwei']
        res_data['sch'] = role_json['sch']
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

        attr = role_json['attr']
        res_data['strong'] = attr['str']
        res_data['body'] = attr['con']
        res_data['quick'] = attr['dex']
        res_data['dodge'] = attr['dog']
        res_data['soul'] = attr['int']
        res_data['mind'] = attr['mind']

        # 门派轻功
        lingskills = role_json['school_qinggong']
        if lingskills is not None and lingskills != 'None':
            calc_data['lignt_menpai'] = 1

        # 英魂
        # lingskills = role_json['multiMS']

        # 元魂珠
        # lingskills = role_json['monster_souls']

        # 灵兽
        # hbs = role_json['hbs']

        # 孩子
        childs = role_json['new_childs']
        haizi_lv, haizi_zizhi, haizi_wuxue = 0, 0, 0
        for child in childs:
            if child['lv'] >= haizi_lv:
                haizi_lv = child['lv']
            if child['potential'] >= haizi_lv:
                haizi_zizhi = child['potential']
            if child['kongfu'] >= haizi_lv:
                haizi_wuxue = child['kongfu']

        calc_data['haizi_lv'] = haizi_lv
        calc_data['haizi_zizhi'] = haizi_zizhi
        calc_data['haizi_wuxue'] = haizi_wuxue

        # 特技
        huikan, dunci, shuifengdu, huoyuan, huxin, wanfeng = 0, 0, 0, 0, 0, 0
        equ = role_json['equ']
        shoushi = ['5', '6', '13', '14', '15', '16', '17', '18']

        for index in shoushi:
            if equ[index].setdefault('ws47', None) is not None:
                huikan += equ[index]['ws47']
            if equ[index].setdefault('ws48', None) is not None:
                dunci += equ[index]['ws48']
            if equ[index].setdefault('ws50', None) is not None:
                huoyuan += equ[index]['ws50']
            if equ[index].setdefault('ws53', None) is not None:
                shuifengdu += equ[index]['ws53']
            if equ[index].setdefault('ws38', None) is not None:
                huxin += equ[index]['ws38']
            if equ[index].setdefault('ws138', None) is not None:
                wanfeng += equ[index]['ws138']

        chibangdesc = role_json['wing_inlay_prop']
        if chibangdesc is not None and '护心' in chibangdesc:
            huxin += 3

        # 觉醒
        final_skill = role_json['final_skill']
        if final_skill is not None:
            calc_data['awake_lv'] = final_skill['lv']
            calc_data['release_lv'] = final_skill['releaseScale']
            calc_data['awake_value'] = final_skill['attrId']

            minglian = final_skill['minglian']
            if minglian is not None:
                calc_data['lianhu'] = minglian['enh2Num']
                calc_data['minglian'] = minglian['changeValue'] + minglian['fixedValue']

            if final_skill['lv'] >= 70:
                subSkills = final_skill['subSkills']
                for subSkill in subSkills:
                    if subSkill['libLv'] == 7:
                        wanfeng += subSkill['lv']

        if huikan >= 10:
            calc_data['huikanfanghu'] = 1
        if dunci >= 10:
            calc_data['duncifanghu'] = 1
        if huoyuan >= 10:
            calc_data['huoyuanfanghu'] = 1
        if shuifengdu >= 10:
            calc_data['shuifengdufanghu'] = 1
        if wanfeng >= 10:
            calc_data['wanfeng'] = 1
        if huxin >= 10:
            calc_data['huxin'] = 1

        # 时装
        xuansu, qinghua, guhong, haitang = 0, 0, 0, 0
        xiangyun, tinglan, canghai, jiangnan = 0, 0, 0, 0
        feitian, tianhu, xianhu = 0, 0, 0
        formated_role_desc = soup.find('textarea', id="formated_role_desc")
        format_role = formated_role_desc.get_text()
        format_role_json = json.loads(format_role, 'utf-8')
        for key, value in format_role_json['clothes_info'].items():
            if '青花' in value['name']:
                qinghua = 1
            if '玄素天成' in value['name']:
                xuansu = 1
            if '孤鸿月影' in value['name']:
                guhong = 1
            if '海棠未雨' in value['name']:
                haitang = 1
            if '思暖' in value['name']:
                xiangyun = 1
            if '汀兰' in value['name']:
                tinglan = 1
            if '沧海桑田' in value['name']:
                canghai = 1
            if '夜雨江南' in value['name']:
                jiangnan = 1
            if '飞天' in value['name']:
                feitian = 1
            if '天狐' in value['name']:
                tianhu = 1
            if '仙狐' in value['name']:
                xianhu = 1

        shizhuang = ['19', '20', '30', '31']
        equ.setdefault('30', None)
        equ.setdefault('31', None)
        equ.setdefault('19', None)
        equ.setdefault('20', None)
        for index in shizhuang:
            if equ[index] is not None:
                equ[index].setdefault('id', None)
                yfid = equ[index]['id']
                if yfid == 21326 or yfid == 21327:
                    xuansu = 1
                if yfid == 21202 or yfid == 21203:
                    qinghua = 1
                if yfid == 21323 or yfid == 21324:
                    guhong = 1
                if yfid == 21335 or yfid == 21336:
                    tinglan = 1
                if yfid == 210000 or yfid == 210001:
                    canghai = 1
                if yfid == 210168 or yfid == 210169:
                    jiangnan = 1
                if yfid == 210037:
                    haitang = 1

        # 包裹
        invs = role_json['inv']
        for key, value in invs.items():
            if value['id'] is None:
                continue
            yfid = value['id']
            if yfid == 21326 or yfid == 21327:
                xuansu = 1
            if yfid == 21202 or yfid == 21203:
                qinghua = 1
            if yfid == 21323 or yfid == 21324:
                guhong = 1
            if yfid == 21335 or yfid == 21336:
                tinglan = 1
            if yfid == 210000 or yfid == 210001:
                canghai = 1
            if yfid == 210168 or yfid == 210169:
                jiangnan = 1
            if yfid == 210037:
                haitang = 1

        calc_data['qinghua'] = qinghua
        calc_data['xuansu'] = xuansu
        calc_data['guhong'] = guhong
        calc_data['xiangyun'] = xiangyun
        calc_data['tinglan'] = tinglan
        calc_data['haitang'] = haitang
        calc_data['feihuhuaqiu'] = feitian
        calc_data['tianhulishang'] = tianhu
        calc_data['xianhucaijue'] = xianhu
        calc_data['canghaisangtian'] = canghai
        calc_data['yeyujiangnan'] = jiangnan

        return res_data, calc_data
