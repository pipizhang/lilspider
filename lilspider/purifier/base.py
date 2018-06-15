# -*- coding: utf-8 -*-
import re

class TextSpaceProcessor(object):

    def __call__(self, content: str) -> str:
        content = re.sub(r'\s{2,}', ' ', content)
        return content

