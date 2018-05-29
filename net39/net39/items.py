# -*- coding: utf-8 -*-

import scrapy

class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    title      = scrapy.Field()
    content    = scrapy.Field()
    url        = scrapy.Field()
    image_urls = scrapy.Field()
    images     = scrapy.Field()
