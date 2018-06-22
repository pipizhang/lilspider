# -*- coding: utf-8 -*-
import re
from lilspider.cleaner.zh import PTextCleaner
from lilspider.cleaner.base import Replace
from lilspider.utils.html import get_cleaner, pretty

class Net39SpecialPurifier(object):

    def __call__(self, content: str) -> str:
        cl = PTextCleaner(content)
        cl.add_pattern('.*39健康网.*转载.*')
        cl.add_pattern('.*实习编辑：.*')
        cl.add_pattern('.*责任编辑：.*')
        cl.add_pattern('.*相关阅读：.*')
        cl.add_pattern('.*推荐阅读：.*')
        cl.add_pattern('.*关注.*微信.*')
        cl.add_pattern('.*扫描.*二维码.*')
        cl.add_pattern('.*医院.*主任.*', 30)
        cl.add_pattern('.*医院.*专家.*', 30)
        cl.add_pattern('^<p><a .*?</a></p>$')
        content = cl.run()
        content = Replace(content, [
            '39健康网.*?转载。'
        ]).run()
        return content

class Net39HtmlPurifier(object):

    def first(self, content: str) -> str:
        c = get_cleaner(content)
        c.safe_attrs('href', 'src')
        c.kill_tags('center', 'ul', 'li')
        return c.clean()

    def second(self, content: str) -> str:
        c = get_cleaner(content)
        c.allow_tags('p', 'div', 'strong')
        return c.clean()

    def __call__(self, content: str) -> str:
        content = self.first(content)
        content = self.second(content)
        content = pretty(content, newline_tags='p div')
        return content

