
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'CbgSpider.settings')
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
process = CrawlerProcess(get_project_settings())
process.crawl("cbg")
process.start()