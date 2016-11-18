# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41


import requests
from bs4 import BeautifulSoup
import traceback
import json


if __name__ == "__main__":
    url = "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail&serverid=161&equip_id=211582"
    requests.adapters.DEFAULT_RETRIES = 3
    headers = {'Content-Type': 'text/plain;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
               'Referer': 'http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search',
               'Origin': 'http://tx3.cbg.163.com'}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            html_cont = response.content
            soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
            role_desc = soup.find('textarea', id="role_desc")
            role = role_desc.get_text()
            role_json = json.loads(role, 'utf-8')
            equ = role_json['equ']
            print('武器=' + str(equ['5']['id']))

            childs = role_json['new_childs']
            for child in childs:
                print(child['equs']['0']['id'])

    except Exception as e:
        print(e, traceback.print_exc())