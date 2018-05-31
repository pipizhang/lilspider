# -*- coding: utf-8 -*-
import re
import lxml.html
import urllib.parse

def url_encode(param: str) -> str:
    return urllib.parse.quote(param)

def url_decode(param: str) -> str:
    return urllib.parse.unquote(param)

def abs_url(base_url: str, relative_url: str) -> str:
    f = f'<a href="{relative_url}"></a>'
    t = lxml.html.make_links_absolute(f, base_url)
    match = re.search(r'href=[\'"]?([^\'" >]+)', t)
    if match is None:
        return ""
    else:
        return match.group(1)


