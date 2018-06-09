# -*- coding: utf-8 -*-
import re
from ..utils import *
from ..purifier.html import HtmlRawPurifier
from .base import PurifierProcessor

class ArticleTitle(PurifierProcessor):

    def __init__(self) -> None:
        pass

    def __call__(self, content: str) -> str:
        content = remove_tags(content)
        content = re.sub(r'\s+', ' ', content)
        content = str.strip(content)
        return content

class ArticleContent(PurifierProcessor):

    purifiers = [
        HtmlRawPurifier()
    ]

