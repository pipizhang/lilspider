# -*- coding: utf-8 -*-
from lilspider.cleaner.base import Replace
from lilspider.processors.base import PurifierProcessor
from lilspider.processors.zh import ArticleTitle
from lilspider.purifier.html import HtmlRawPurifier
from lilspider.purifier.base import TextSpaceProcessor
from .purifier import Net39SpecialPurifier, Net39HtmlPurifier

class Net39ArticleTitle(PurifierProcessor):

    def __call__(self, content: str) -> str:
        content = ArticleTitle()(content)
        content = Replace(content, [
            '39健康网'
        ]).run()
        return content

class Net39ArticleContent(PurifierProcessor):

    purifiers = [
        HtmlRawPurifier(),
        Net39SpecialPurifier(),
        Net39HtmlPurifier(),
        TextSpaceProcessor()
    ]

