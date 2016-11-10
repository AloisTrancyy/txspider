# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41

import html_downloader
import html_parser


class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def craw(self, url):
        try:
            html_cont = self.downloader.download(url)
            new_data = self.parser.parse(html_cont)
            with open('format_data.json', 'wb') as f:
                try:
                    f.write(str(new_data))
                except Exception as e:
                    print e
                finally:
                    f.close()
        except Exception as e:
            print 'craw failed:', e


if __name__ == "__main__":
    root_url = "http://tx3.cbg.163.com/cgi-bin/equipquery.py?act=overall_search_show_detail&serverid=15&equip_id=392061"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
