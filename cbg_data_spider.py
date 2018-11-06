# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import datetime
import json
import time

import pymysql
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup

import config


class RoleSpider(object):
    rows = set()

    def craw(self):
        for row in self.rows:
            time.sleep(3)
            url = row['url']
            role_id = row['id']
            try:
                connection = pymysql.connect(**config.dbconfig)
                with connection.cursor() as cursor:
                    query = 'select count(1) as count from cbg_data where role_id=' + str(role_id)
                    cursor.execute(query)
                    if cursor.fetchone()['count'] == 0:
                        html_cont = self.download_html(url)
                        basic_data = self.parse_html(html_cont, role_id)
                        sql = 'INSERT INTO cbg_data (role_id'
                        for key, value in basic_data.items():
                            if key == 'role_id' or key == 'pass_date' or value is None:
                                continue
                            sql = sql + ',' + key
                        sql = sql + ' ) values (' + str(basic_data['role_id'])
                        for key, value in basic_data.items():
                            if key == 'role_id' or key == 'pass_date' or value is None:
                                continue
                            if type(value) == int or type(value) == float:
                                sql = sql + ',' + str(value)
                            else:
                                sql = sql + ',\'' + str(value.encode('utf-8').decode("utf-8")) + '\''
                        sql += ')'
                        print(sql)
                        cursor.execute(sql)
                        # 设置角色已爬取
                        pass_date = basic_data.get('pass_date')
                        if pass_date is None:
                            update_craw = 'update cbg_role set craw = 1,yn=0 where id = ' + str(role_id)
                            print(update_craw)
                            cursor.execute(update_craw)
                        else:
                            update_craw = 'update cbg_role set craw = 1,exp_time =\'' + basic_data[
                                'pass_date'] + '\' where id = ' + str(role_id)
                            print(update_craw)
                            cursor.execute(update_craw)
                    else:
                        update_craw = 'update cbg_role set craw = 1,yn=0 where id = ' + str(role_id)
                        print(update_craw)
                        cursor.execute(update_craw)
                connection.commit()
            except Exception as ex:
                pass
            finally:
                connection.close()

    def has_new_url(self):
        return len(self.new_url) != 0

    def add_new_url(self, url):
        if url not in self.new_url:
            self.new_url.add(url)

    def get_new_url(self):
        return self.new_url.pop()

    def download_html(self, url):
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Referer': 'http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search'
        }
        requests.adapters.DEFAULT_RETRIES = 3
        response = requests.get(url, headers=headers, timeout=3)
        print('craw:' + url)
        if response.status_code != 200:
            return None
        response.encoding = 'utf-8'  # 显式地指定网页编码，一般情况可以不用
        return response.content

    def parse_html(self, html_cont, equip_id):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb18030')
        new_data = self.get_new_data(soup, equip_id)
        return new_data

    def get_new_data(self, soup, role_id):
        res_data = {}
        res_data['role_id'] = role_id

        pass_date_td = soup.find_all('span', class_="b")
        for td in pass_date_td:
            if '出售剩余时间' in td.get_text():
                pass_date = get_exp_time(td.parent.get_text().replace('出售剩余时间：', ''))
                res_data['pass_date'] = pass_date
        role_desc = soup.find('textarea', id="role_desc")
        role = role_desc.get_text()
        role_json = json.loads(role)
        # 基础信息
        role_json.setdefault('fly_soul_phase', None)
        role_json.setdefault('fly_soul_lv', None)
        role_json.setdefault('cri_add_p', None)
        role_json.setdefault('cri_sub_p', None)
        role_json.setdefault('absolutely_attack', None)
        role_json.setdefault('absolutely_defence', None)
        role_json.setdefault('thump_sub_p', None)
        role_json.setdefault('thump_add_p', None)
        role_json.setdefault('final_skill', None)
        fly_soul_phase = role_json['fly_soul_phase']
        fly_soul_lv = role_json['fly_soul_lv']

        level = role_json['lv']
        if fly_soul_phase is not None:
            if int(fly_soul_phase) == 1:
                res_data['fly_soul_phase'] = '地魂'
            if int(fly_soul_phase) == 2:
                res_data['fly_soul_phase'] = '天魂'
        res_data['fly_soul_lv'] = fly_soul_lv
        res_data['lv'] = level
        res_data['mhp'] = role_json['mhp']
        res_data['msp'] = role_json['msp']
        res_data['critical'] = role_json['critical']
        res_data['sex'] = role_json['sex']
        res_data['fly_soul_phase'] = fly_soul_phase
        res_data['fly_soul_lv'] = fly_soul_lv
        res_data['xiuwei'] = role_json['xiuwei']
        res_data['equ_xiuwei'] = role_json['equ_xiuwei']
        res_data['sch'] = role_json['sch']
        res_data['pattack_max'] = role_json['pattack_max']
        res_data['mattack_max'] = role_json['mattack_max']
        res_data['pattack_min'] = role_json['pattack_min']
        res_data['mattack_min'] = role_json['mattack_min']
        res_data['hit'] = role_json['hit']
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
        role_json.setdefault('school_qinggong', None)
        lingskills = role_json['school_qinggong']
        if lingskills is not None and lingskills != 'None':
            res_data['lignt_menpai'] = 1

        # 英魂
        # lingskills = role_json['multiMS']

        # 元魂珠
        monster_souls = role_json['monster_souls']
        for key, value in monster_souls.items():
            prototype = value['prototype']
            if prototype == 4772:
                res_data['mawangye'] = 1
            if prototype == 5207:
                res_data['wanshengtianzun'] = 1
            if prototype == 5037:
                res_data['yehuo'] = 1
            if prototype == 5054:
                res_data['xiyangyang'] = 1
            if prototype == 5274:
                res_data['mourixingguan'] = 1
            if prototype == 3117 or prototype == 4657:
                value.setdefault('skills_lv', None)
                skills_lv = value['skills_lv']
                if skills_lv is None:
                    continue
                for sk, level in skills_lv.items():
                    if sk == '4436':
                        res_data['dulanggui'] = 1

        # 灵兽
        # hbs = role_json['hbs']

        # 孩子
        childs = role_json.get('new_childs')
        haizi_lv, haizi_zizhi, haizi_wuxue, haizi_jiahu = 0, 0, 0, 0
        if childs is not None and len(childs) > 0:
            for child in childs:
                if child['lv'] >= haizi_lv:
                    haizi_lv = child['lv']
                if child['potential'] >= haizi_zizhi:
                    haizi_zizhi = child['potential']
                if child['kongfu'] >= haizi_wuxue:
                    haizi_wuxue = child['kongfu']

                child.setdefault('equs', None)
                equs = child['equs']
                if equs is None:
                    continue
                equs.setdefault('0', None)
                if equs['0'] is not None and equs['0']['id'] in (
                        1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1808, 1836, 150012):
                    res_data['haizi_tiayu'] = 1

                if child.get('equs') is not None:
                    for key, value in child['equs'].items():
                        if value is not None and value.get('cenh') is not None:
                            haizi_jiahu += value['cenh']

        res_data['haizi_lv'] = haizi_lv
        res_data['haizi_zizhi'] = haizi_zizhi
        res_data['haizi_wuxue'] = haizi_wuxue
        res_data['haizi_jiahu'] = haizi_jiahu

        # 特技
        huikan, dunci, shuifengdu, huoyuan, huxin, wanfeng = 0, 0, 0, 0, 0, 0
        equ = role_json['equ']
        shoushi = ['6', '7', '13', '14', '15', '16', '17', '18']

        for index in shoushi:
            equ.setdefault(index, None)
            if equ[index] is None:
                continue
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

        if role_json['sch'] == 2:
            yifu = ['0', '1', '2', '3', '8', '9', '10', '11']
            zhendan = [2266, 2268, 2272, 2269, 2267, 2271, 2270, 2273]
            zhendan_count = 0
            for index in yifu:
                equ.setdefault(index, None)
                if equ[index] is None:
                    continue
                if equ[index]['id'] in zhendan:
                    zhendan_count += 1
            if zhendan_count >= 2 and zhendan_count < 4:
                huxin += 5
            elif zhendan_count >= 4:
                huxin += 10

        chibangdesc = role_json.get('wing_inlay_prop')
        if chibangdesc is not None and '护心' in chibangdesc:
            huxin += 3

        if equ.setdefault('4', None) is not None:
            if equ['4']['id'] in [22374, 22375, 22376, 22377, 22378, 22379, 22380, 22381, 22502]:
                res_data['shilifushou'] = 1

        if equ.setdefault('5', None) is not None:
            if equ['5']['id'] in [1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1963, 1967]:
                res_data['taichu'] = 1
            if equ['5']['id'] in [1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1808, 1836, 150012]:
                res_data['renwu_tianyu'] = 1
        # print(equ['5'])
        # print('武器=' + str(equ['5']['id']))
        # print('副手=' + str(equ['4']['id']))

        # 觉醒
        final_skill = role_json['final_skill']
        if final_skill is not None:
            res_data['awake_lv'] = final_skill['lv']
            res_data['release_lv'] = final_skill['releaseScale']
            res_data['awake_value'] = final_skill['attrId']

            minglian = final_skill['minglian']
            if minglian is not None:
                res_data['lianhu'] = minglian['enh2Num']
                res_data['minglian'] = minglian['changeValue'] + minglian['fixedValue']

            if final_skill['lv'] >= 70:
                subSkills = final_skill['subSkills']
                for subSkill in subSkills:
                    if subSkill['libLv'] == 7:
                        wanfeng += subSkill['lv']

        if huikan >= 10:
            res_data['huikanfanghu'] = 1
        if dunci >= 10:
            res_data['duncifanghu'] = 1
        if huoyuan >= 10:
            res_data['huoyuanfanghu'] = 1
        if shuifengdu >= 10:
            res_data['shuifengdufanghu'] = 1
        if wanfeng >= 10:
            res_data['wanfeng'] = 1
        if huxin >= 10:
            res_data['huxin'] = 1

        res_data['jinbi'] = role_json['cash'].replace('金', '.').replace('银', '').replace('铜', '')
        # 大禹
        if role_json['credit'].get('22') is None:
            res_data['dayu'] = 0
        else:
            res_data['dayu'] = role_json['credit'].get('22')
        # 军姿
        if role_json['credit'].get('26') is None:
            res_data['junzi'] = 0
        else:
            res_data['junzi'] = role_json['credit'].get('26')
        # 天域
        if role_json['credit'].get('35') is None:
            res_data['tianyu'] = 0
        else:
            res_data['tianyu'] = role_json['credit'].get('35')

        # 元宝
        if role_json.get('coinA') is None:
            res_data['yuanbao'] = 0
        else:
            res_data['yuanbao'] = role_json['coinA']

        # 时装
        xuansu, qinghua, guhong, haitang = 0, 0, 0, 0
        xiangyun, tinglan, canghai, jiangnan = 0, 0, 0, 0
        feitian, tianhu, xianhu = 0, 0, 0
        bihai, changong, changkong, fengyuzihuang = 0, 0, 0, 0
        shuyinghengxie = 0
        formated_role_desc = soup.find('textarea', id="formated_role_desc")
        format_role = formated_role_desc.get_text()
        format_role_json = json.loads(format_role)
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
            if '碧海惊涛' in value['name']:
                bihai = 1
            if '鹰击长空' in value['name']:
                changkong = 1
            if '蟾宫折桂' in value['name']:
                changong = 1
            if '凤羽紫凰' in value['name']:
                fengyuzihuang = 1
            if '疏影横斜' in value['name']:
                shuyinghengxie = 1

        shizhuang = ['19', '20', '30', '31']
        equ.setdefault('30', None)
        equ.setdefault('31', None)
        equ.setdefault('19', None)
        equ.setdefault('20', None)
        for index in shizhuang:
            if equ[index] is not None:
                equ[index].setdefault('id', None)
                yfid = equ[index]['id']
                if yfid == 21121 or yfid == 21122 or yfid == 21123 or yfid == 21124 or yfid == 21326 or yfid == 21327\
                        or yfid == 88326 or yfid == 88327:
                    #21121,21122,21123,21124,21326,21327,88326,88327
                    xuansu = 1
                if yfid == 21189 or yfid == 21190 or yfid == 21202 or yfid == 21203 or yfid == 121533 or yfid == 121534\
                        or yfid == 121572 or yfid == 121573:
                    #21189,21190,21202,21203,121533,121534,121572,121573
                    qinghua = 1
                if yfid == 21293 or yfid == 21294 or yfid == 21323 or yfid == 21324 or yfid == 121576 or yfid == 121577:
                    #21293,21294,21323,21324,121576,121577
                    guhong = 1
                if yfid == 21335 or yfid == 21336 or yfid == 121529 or yfid == 121530:
                    #21335,21336,121529,121530
                    tinglan = 1
                if yfid == 21339 or yfid == 21340 or yfid == 121531 or yfid == 121532:
                    # 21339, 21340, 121531, 121532
                    xiangyun = 1
                if yfid == 210000 or yfid == 210001 or yfid == 210002 or yfid == 210003 or yfid == 210004 or yfid == 210005:
                    #210000,210001,210002,210003,210004,210005
                    canghai = 1
                if yfid == 210168 or yfid == 210169:
                    jiangnan = 1
                if yfid == 121705 or yfid == 121706 or yfid == 210037 or yfid == 210039 or yfid == 210040 \
                        or yfid == 210073 or yfid == 210074:
                    #121705,121706,210037,210038,210039,210040,210073,210074
                    haitang = 1

                if yfid == 210046 or yfid == 210047 or yfid == 210146 or yfid == 210147:
                    feitian = 1
                if yfid == 210148 or yfid == 210149 or yfid == 210210 or yfid == 210211:
                    #210148,210149,210210,210211
                    tianhu = 1
                if yfid == 210144 or yfid == 210145 or yfid == 210206 or yfid == 210207:
                    #210144,210145,210206,210207
                    xianhu = 1
                if yfid == 88454 or yfid == 88455 or yfid == 88511:
                    bihai = 1
                if yfid == 21449 or yfid == 21450:
                    changkong = 1
                if yfid == 21487 or yfid == 21488 or yfid == 121515 or yfid == 121516 or yfid == 121580 or yfid == 121581:
                    #21487,21488,121515,121516,121580,121581
                    changong = 1
                if yfid == 21399 or yfid == 21400:
                    #21399,21400,88331,88332
                    fengyuzihuang = 1
                if yfid == 121745 or yfid == 121746 or yfid == 121747 or yfid == 121748 or \
                                yfid == 121749 or yfid == 121750 or yfid == 121751 or yfid == 121752:
                    #121745,121746,121747,121748,121749,121750,121751,121752
                    shuyinghengxie = 1

        # 包裹
        invs = role_json['inv']
        for key, value in invs.items():
            if value['id'] is None:
                continue
            yfid = value['id']
            if yfid == 170087 or yfid == 170041:
                res_data['qianyang'] = 1
            elif yfid == 170079 or yfid == 170033:
                    res_data['moyinli'] = 1
            elif yfid == 170078 or yfid == 170032:
                    res_data['mudanyuan'] = 1
            elif yfid == 170081 or yfid == 170035:
                    res_data['yinglongya'] = 1
            elif yfid == 170080 or yfid == 170034:
                    res_data['xuelongya'] = 1

            if yfid == 24165:
                res_data['honglian'] = value['cwrap']
            elif yfid == 64103 or yfid == 4164 or yfid == 24164:
                res_data['leizuan'] = value['cwrap']

            if yfid == 63669:
                res_data['vip9'] = 1
            if yfid == 21121 or yfid == 21122 or yfid == 21123 or yfid == 21124 or yfid == 21326 or yfid == 21327 \
                    or yfid == 88326 or yfid == 88327:
                # 21121,21122,21123,21124,21326,21327,88326,88327
                xuansu = 1
            if yfid == 21189 or yfid == 21190 or yfid == 21202 or yfid == 21203 or yfid == 121533 or yfid == 121534 \
                    or yfid == 121572 or yfid == 121573:
                # 21189,21190,21202,21203,121533,121534,121572,121573
                qinghua = 1
            if yfid == 21293 or yfid == 21294 or yfid == 21323 or yfid == 21324 or yfid == 121576 or yfid == 121577:
                # 21293,21294,21323,21324,121576,121577
                guhong = 1
            if yfid == 21335 or yfid == 21336 or yfid == 121529 or yfid == 121530:
                # 21335,21336,121529,121530
                tinglan = 1
            if yfid == 21339 or yfid == 21340 or yfid == 121531 or yfid == 121532:
                # 21339, 21340, 121531, 121532
                xiangyun = 1
            if yfid == 210000 or yfid == 210001 or yfid == 210002 or yfid == 210003 or yfid == 210004 or yfid == 210005:
                # 210000,210001,210002,210003,210004,210005
                canghai = 1
            if yfid == 210168 or yfid == 210169:
                jiangnan = 1
            if yfid == 121705 or yfid == 121706 or yfid == 210037 or yfid == 210039 or yfid == 210040 \
                    or yfid == 210073 or yfid == 210074:
                # 121705,121706,210037,210038,210039,210040,210073,210074
                haitang = 1
            if yfid == 210046 or yfid == 210047 or yfid == 210146 or yfid == 210147:
                feitian = 1
            if yfid == 210148 or yfid == 210149 or yfid == 210210 or yfid == 210211:
                # 210148,210149,210210,210211
                tianhu = 1
            if yfid == 210144 or yfid == 210145 or yfid == 210206 or yfid == 210207:
                # 210144,210145,210206,210207
                xianhu = 1
            if yfid == 88454 or yfid == 88455 or yfid == 88511:
                bihai = 1
            if yfid == 21449 or yfid == 21450:
                changkong = 1
            if yfid == 21487 or yfid == 21488 or yfid == 121515 or yfid == 121516 or yfid == 121580 or yfid == 121581:
                # 21487,21488,121515,121516,121580,121581
                changong = 1
            if yfid == 21399 or yfid == 21400:
                # 21399,21400,88331,88332
                fengyuzihuang = 1
            if yfid == 121745 or yfid == 121746 or yfid == 121747 or yfid == 121748 or \
                            yfid == 121749 or yfid == 121750 or yfid == 121751 or yfid == 121752:
                # 121745,121746,121747,121748,121749,121750,121751,121752
                shuyinghengxie = 1

        res_data['qinghua'] = qinghua
        res_data['xuansu'] = xuansu
        res_data['guhong'] = guhong
        res_data['xiangyun'] = xiangyun
        res_data['tinglan'] = tinglan
        res_data['haitang'] = haitang
        res_data['feihuhuaqiu'] = feitian
        res_data['tianhulishang'] = tianhu
        res_data['xianhucaijue'] = xianhu
        res_data['canghaisangtian'] = canghai
        res_data['yeyujiangnan'] = jiangnan
        res_data['bihai'] = bihai
        res_data['changkong'] = changkong
        res_data['changong'] = changong
        res_data['fengyuzihuang'] = fengyuzihuang
        res_data['shuyinghengxie'] = shuyinghengxie
        return res_data

def get_exp_time(exp_time):
    day, hour, minute = 0, 0, 0
    if '天' in exp_time:
        day = exp_time[0:exp_time.index("天")]
        hour = exp_time[exp_time.index("天") + 1:exp_time.index('时')]
        minute = 30
    else:
        if '时' in exp_time:
            hour = exp_time[0:exp_time.index('时')]
            minute = 0
    now = datetime.datetime.now()
    date = now + datetime.timedelta(days=int(day)) + datetime.timedelta(hours=int(hour)) + datetime.timedelta(
        minutes=int(minute))
    return date.strftime('%Y-%m-%d %H:%M:%S')


def data_job():
    print("role job start! time = " + str(datetime.datetime.now()))
    obj_spider = RoleSpider()
    connection = pymysql.connect(**config.dbconfig)
    try:
        with connection.cursor() as cursor:
            sql = 'select id,url from cbg_role where yn=1 and craw = 0'
            cursor.execute(sql)
            obj_spider.rows = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(e)
        pass
    finally:
        connection.close()
    obj_spider.craw()

if __name__ == "__main__":
    serverScheduler = BlockingScheduler()
    serverScheduler.add_job(data_job, 'interval', hours=2)
    serverScheduler.start()
    # role_job()
