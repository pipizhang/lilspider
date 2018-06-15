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

def test_url_decode(capsys: Any) -> None:
    assert url_decode('hello%20world') == 'hello world'

def test_remove_empty_tags(capsys: Any) -> None:
    html = '<p>lilspider<strong></strong></p>'
    assert remove_tags(html) == 'lilspider'

def test_remove_tags(capsys: Any) -> None:
    html = """
        <html>
        <body class="main">
          <h1>rocket man</h1>
        </body>
        </html>
    """
    assert remove_tags(html) == 'rocket man'
    assert html2text(html) == 'rocket man'

def test_inner_trim(capsys: Any) -> None:
    html1 = '<p> a<strong> b </strong></p>'
    html2 = '<p> a<i> b </i></p>'
    assert inner_trim(html1) == '<p>a<strong>b</strong></p>'
    assert inner_trim(html2) != '<p>a<i>b</i></p>'
    assert inner_trim(html2, 'p i'.split()) == '<p>a<i>b</i></p>'
    assert inner_trim(html2, 'p'.split()) == '<p>a<i> b </i></p>'
