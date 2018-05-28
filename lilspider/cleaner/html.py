# -*- coding: utf-8 -*-
from typing import TypeVar, Any
from lxml.html.clean import Cleaner
from lxml import etree

__all__ = ['HtmlCleaner']

T = TypeVar('T', bound='HtmlCleaner')
class HtmlCleaner(object):

    def __init__(self, content: str="") -> None:
        self.__style = True
        self.__links = True
        self.__page_structure = False
        self.__safe_attrs_only = True
        self.__allow_tags = None # type: Any
        self.__kill_tags = None # type: Any
        self.__remove_tags = None # type: Any
        self.__safe_attrs = ['href', 'src'] # type: Any
        self.__input = content

    def input(self: T, content: str) -> T:
        self.__input = content
        return self

    def get(self) -> str:
        return self.__input

    def style(self: T, enable: bool) -> T:
        self.__style = enable
        return self

    def links(self: T, enable: bool) -> T:
        self.__links = enable
        return self

    def page_structure(self: T, enable: bool) -> T:
        self.__page_structure = enable
        return self

    def allow_tags(self: T, *args: str) -> T:
        self.__allow_tags = args
        return self

    def kill_tags(self: T, *args: str) -> T:
        self.__kill_tags = args
        return self

    def remove_tags(self: T, *args: str) -> T:
        self.__remove_tags = args
        return self

    def safe_attrs(self: T, *args: str) -> T:
        self.__safe_attrs = args
        return self

    def safe_attrs_only(self: T, enable: bool) -> T:
        self.__safe_attrs_only = enable
        return self

    def clean(self: T) -> str:
        cleaner = Cleaner()
        cleaner.style = self.__style
        cleaner.links = self.__links
        cleaner.page_structure = self.__page_structure
        cleaner.safe_attrs_only = self.__safe_attrs_only

        if self.__allow_tags is not None: cleaner.allow_tags = self.__allow_tags
        if self.__kill_tags is not None: cleaner.kill_tags = self.__kill_tags
        if self.__remove_tags is not None: cleaner.remove_tags = self.__remove_tags
        if self.__safe_attrs is not None: cleaner.safe_attrs = self.__safe_attrs

        self.__input = cleaner.clean_html(self.__input)
        return self.__input

