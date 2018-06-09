# -*- coding: utf-8 -*-
from typing import List

class PurifierProcessor(object):
    """ A processor consists of multiple purifier """

    purifiers = [] # type:List

    def add_purifier(self, purifier: object) -> None:
        self.purifiers.append(purifier)

    def run(self, content: str) -> str:
        for p in self.purifiers:
            content = p(content)
        return content

    def __call__(self, content: str) -> str:
        return self.run(content)

