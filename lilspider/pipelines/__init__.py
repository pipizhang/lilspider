# -*- coding: utf-8 -*-
from typing import List
import scrapy
import logging

class ItemDebugPipeline(object):
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider) -> List:
        for k, v in item.items():
            spider.log('{}: {}'.format(k, v), logging.INFO)
        return item

