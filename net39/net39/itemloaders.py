# -*- coding: utf-8 -*-
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Compose, Join

from lilspider.processors import CommonArticleTitle, CommonArticleContent
from .items import ArticleItem

class ArticleItemLoader(ItemLoader):

    default_item_class = ArticleItem
    default_output_processor = TakeFirst()

    title_out = Compose(TakeFirst(), CommonArticleTitle())
    content_out = Compose(Join(''), CommonArticleContent())

class BlogItemLoader(ArticleItemLoader):
    pass

