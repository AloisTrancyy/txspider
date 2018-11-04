# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urljoin


class CbgSpider(scrapy.Spider):
    name = 'cbg'
    allowed_domains = ['tx3-ios2.cbg.163.com']
    start_urls = [
        'http://tx3-ios2.cbg.163.com/cbg-center/search.py?num_per_page=15&products=tx2&act=basic_search_role&order_refer=8&price_min=50000&price_max=29999900&level_min=69&level_max=69&school=1&page=1']

    def parse(self, response):
        base_url = 'http://tx3-ios2.cbg.163.com/cbg-center/search.py?num_per_page=15&products=tx2&act=basic_search_role&order_refer=8&price_min=50000&price_max=29999900&level_min=69&level_max=69&school=1&page=1'

        old_url = response.url
        url_parsed = urlparse(old_url)
        page = parse_qs(url_parsed.query)["page"]
        school = parse_qs(url_parsed.query)["school"]

        result = json.loads(response.body)  # 将Json格式数据处理为字典类型
        items = result.get("equip_list")
        if len(items) == 0:
            next_url = urljoin(base_url, "&page=" + str(int(page) + 1))
            next_url = urljoin(next_url, "&school=" + str(int(school) + 1))
            print(next_url)
            yield scrapy.FormRequest(
                url=next_url,
                # formdata={"modelCode": item['seriesId'], "agent": "7"},
                callback=self.parse,
                dont_filter=True
            )
        else:
            for item in items:
                next_url = urljoin(old_url, "&school=" + str(int(school) + 1))
                print(next_url)
                yield scrapy.FormRequest(
                    url=next_url,
                    callback=self.parse,
                    dont_filter=True
                )

    def parse_role(self, response):
        pass
