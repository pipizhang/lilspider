# -*- coding: utf-8 -*-
import re
from lilspider.cleaner import HtmlCleaner

class ArticlePipeline(object):
    def process_item(self, item, spider):
        self._title(item)
        self._content(item)
        return item

    def _title(self, item):
        item['title'] = item['title']

    def _content(self, item):
        item['content'] = item['content']


