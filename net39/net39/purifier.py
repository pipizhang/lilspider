# -*- coding: utf-8 -*-
import re
from lilspider.cleaner.zh import PTextCleaner

class Net39SpecialPurifier(object):

    def __call__(self, content: str) -> str:
        cl = PTextCleaner(content)
        cl.add_pattern('.*39健康网.*转载.*')
        cl.add_pattern('.*实习编辑：.*')
        cl.add_pattern('.*相关阅读：.*')
        cl.add_pattern('.*推荐阅读：.*')
        cl.add_pattern('^<p><a .*?</a></p>$')
        return cl.run()

