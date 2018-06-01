# -*- coding: utf-8 -*-
import re
import scrapy

class ProxyMiddleware(object):
    """Inject proxy settings for HttpProxyMiddleware"""

    def process_request(self, request: scrapy.http.Request, spider: scrapy.spiders.Spider) -> None:
        _proxy = spider.settings.get('HTTPPROXY_ADDRESS')
        if type(_proxy) is str and re.match(r'^http', _proxy):
            request.meta['proxy'] = _proxy

