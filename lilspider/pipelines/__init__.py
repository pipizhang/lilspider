# -*- coding: utf-8 -*-
import re
import scrapy
import logging
from typing import List
from ..utils import get_soup

class ItemDebugPipeline(object):

    """Print item for debug"""

    def process_item(self, item: scrapy.Item, spider: scrapy.Spider) -> List:
        for k, v in item.items():
            spider.log('{}: {}'.format(k, v), logging.INFO)
        return item

class ImagePipeline(object):

    """Extract images from content, replace img tags with placeholder and populagte 'image_urls' for download"""

    def process_item(self, item: scrapy.Item, spider: scrapy.Spider) -> List:
        if 'content' in item:
            s = get_soup(item['content'])
            images = s.select('img')
            if len(images):
                item['image_urls'] = [x['src'] for x in images]
                item['content'] = re.sub(r'<img src=[^>]+\>', '{{@IMG}}', item['content'])
            else:
                item['image_urls'] = []
        return item

