# -*- coding: utf-8 -*-
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose, Join

from lilspider.processors.zh import ArticleTitle, ArticleContent
from .items import ArticleItem

class ArticleItemLoader(ItemLoader):

    default_item_class = ArticleItem
    default_output_processor = TakeFirst()

    title_out = Compose(TakeFirst(), ArticleTitle())
    content_out = Compose(Join(''), ArticleContent())

class BlogItemLoader(ArticleItemLoader):
    pass

