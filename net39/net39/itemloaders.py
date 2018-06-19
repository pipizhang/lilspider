# -*- coding: utf-8 -*-
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose, Join
from .processors import Net39ArticleTitle, Net39ArticleContent
from .items import ArticleItem

class ArticleItemLoader(ItemLoader):

    default_item_class = ArticleItem
    default_output_processor = TakeFirst()

    title_out = Compose(TakeFirst(), Net39ArticleTitle())
    content_out = Compose(Join(''), Net39ArticleContent())

class BlogItemLoader(ArticleItemLoader):
    pass

