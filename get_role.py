# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
import requests
import json
from bs4 import BeautifulSoup

url="https://tx3.cbg.163.com/cgi-bin/equipquery.py?act=buy_show_by_ordersn&server_id=161&ordersn=4a99f77a-c3d3-11e8-8051-ecb1d7a5d890"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Referer': 'http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search'
}
requests.adapters.DEFAULT_RETRIES = 3
response = requests.get(url, headers=headers, timeout=3)
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='gb18030')

role_desc = soup.find('textarea', id="role_desc")
role = role_desc.get_text()
role_json = json.loads(role)
print(role_json)