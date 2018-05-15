# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys

from scrapy.exceptions import DropItem
from scrapy.spiders import Spider
from scrapy import Item

from lilspider import checker

class BaiduPipeline(object):
    def process_item(self, item: Item, spider: Spider) -> Item:
        if item['title']:
            print('Title: {}'.format(item['title']))
        if item['url']:
            print('URL: {}'.format(item['url']))

        return item

class Blog39NetPipeline(object):
    def process_item(self, item: Item, spider: Spider) -> Item:
        if spider.name != 'blog.39.net': return item

        try:
            checker.Regex('^blog\.39\.net\/\w+', item['showurl']).run()
            checker.UnInclude('广州', item['title']).run()
            checker.UnInclude('石家庄', item['title']).run()
            checker.UnInclude('武汉', item['title']).run()

            return item
        except:
            raise DropItem(sys.exc_info()[0])


