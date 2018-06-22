# -*- coding: utf-8 -*-
import re
from ..utils import *
from ..purifier.base import TextSpaceProcessor
from ..purifier.html import HtmlRawPurifier
from .base import PurifierProcessor
from ..checker.zh import TitleTextChecker
from ..exceptions import CheckerError

class ArticleTitle(PurifierProcessor):

    def __init__(self) -> None:
        pass

    def __call__(self, content: str) -> str:
        try:
            TitleTextChecker(content).run()
        except CheckerError:
            return ""

        content = html2text(content)
        content = re.sub(r'\s{2,}', ' ', content)
        content = str.strip(content)
        return content

