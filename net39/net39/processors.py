# -*- coding: utf-8 -*-
from lilspider.processors.base import PurifierProcessor
from lilspider.purifier.html import HtmlRawPurifier, HtmlSafePurifier
from lilspider.purifier.base import TextSpaceProcessor
from .purifier import Net39SpecialPurifier

class Net39ArticleTitle(PurifierProcessor):

    def __init__(self) -> None:
        pass

    def __call__(self, content: str) -> str:
        return content

class Net39ArticleContent(PurifierProcessor):

    purifiers = [
        HtmlRawPurifier(),
        Net39SpecialPurifier(),
        HtmlSafePurifier(),
        TextSpaceProcessor()
    ]

