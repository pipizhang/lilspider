# -*- coding: utf-8 -*-
from ..utils import get_cleaner, pretty, remove_tags

class CommonArticleTitle(object):
    """
        Clean the original title content
        Include: trim
    """
    def __init__(self) -> None:
        pass

    def __call__(self, content: str) -> str:
        content = remove_tags(content)
        content = str.strip(content)
        return content

class CommonArticleContent(object):
    """
        Clean the original html content
        Include: remove unsafe tags, pretty format
    """
    def __init__(self) -> None:
        self.c = get_cleaner()
        self.c.safe_attrs('href', 'src')
        self.c.kill_tags('center')
        self.c.remove_tags('a', 'span', 'font', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6')

    def __call__(self, content: str) -> str:
        self.c.input(content)
        content = self.c.clean()
        content = pretty(content, newline_tags='p div')
        return content

