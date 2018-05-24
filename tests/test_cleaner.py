# -*- coding: utf-8 -*-
import pytest
from typing import Any
from lilspider.cleaner import *

def test_replace(capsys: Any) -> None:
    assert 'GOOgle.cOm' == Replace('Google.com', 'o', 'O').run()
    assert '谷歌.com' == Replace('Google.com', 'Google', '谷歌').run()
    assert '谷歌.com' == Replace('Google.com', {'Goo':'谷', 'gle':'歌'}).run()
    assert 'H-ll- W-rld' == Replace('Hello World', ['e', 'o'], '-').run()
    assert 'Hll Wrld' == Replace('Hello World', ['e', 'o']).run()

def test_replace_once(capsys: Any) -> None:
    assert ' This is a title [ZT]' == ReplaceOnce('ZT This is a title [ZT]', 'ZT').run()
