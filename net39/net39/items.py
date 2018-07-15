# -*- coding: utf-8 -*-

import scrapy

class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    title       = scrapy.Field()
    content     = scrapy.Field()
    url         = scrapy.Field()
    image_urls  = scrapy.Field()
    images      = scrapy.Field()
    provider    = scrapy.Field()
    consumer    = scrapy.Field()
    created_at  = scrapy.Field()
    updated_at  = scrapy.Field()
    indexed_at  = scrapy.Field()
    consumed_at = scrapy.Field()
