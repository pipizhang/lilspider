# -*- coding: utf-8 -*-
from lilspider.processor.base import PurifierProcessor
from lilspider.purifier.html import HtmlRawPurifier

class Net39Content(PurifierProcessor):

    purifiers = [
        HtmlRawPurifier()
    ]

