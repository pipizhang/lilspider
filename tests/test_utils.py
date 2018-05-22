# -*- coding: utf-8 -*-
import pytest
from typing import Any
from lilspider.utils import *

def test_abs_url(capsys: Any) -> None:
    assert abs_url('http://example.com/about/', 'wiki/python.html') == 'http://example.com/about/wiki/python.html'
    assert abs_url('http://example.com/about/', '../wiki/python.html') == 'http://example.com/wiki/python.html'
    assert abs_url('https://example.com/', './css/main.css?size=1') == 'https://example.com/css/main.css?size=1'

def test_url_encode(capsys: Any) -> None:
    assert url_encode('hello world') == 'hello%20world'

def test_url_encode(capsys: Any) -> None:
    assert url_decode('hello%20world') == 'hello world'

