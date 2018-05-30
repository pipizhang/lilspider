# -*- coding: utf-8 -*-
import re
import logging
import warnings

from scrapy import signals
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse_cached

logger = logging.getLogger(__name__)

class DisallowDomainMiddleware(object):

    def __init__(self, stats): # type: ignore
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler): # type: ignore
        o = cls(crawler.stats)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def process_spider_output(self, response, result, spider): # type: ignore
        for x in result:
            if isinstance(x, Request):
                if x.dont_filter or self.should_follow(x, spider):
                    yield x
                else:
                    domain = urlparse_cached(x).hostname
                    if domain and domain not in self.domains_seen:
                        self.domains_seen.add(domain)
                        logger.debug("Filtered offsite request to %(domain)r: %(request)s",
                                     {'domain': domain, 'request': x}, extra={'spider': spider})
                        self.stats.inc_value('offsite/domains', spider=spider)
                    self.stats.inc_value('offsite/filtered', spider=spider)
            else:
                yield x

    def should_follow(self, request, spider): # type: ignore
        regex = self.host_regex
        if regex is None:
            return True
        # hostname can be None for wrong urls (like javascript links)
        host = urlparse_cached(request).hostname or ''
        return not bool(regex.search(host))

    def get_host_regex(self, spider): # type: ignore
        """Override this method to implement a different offsite policy"""
        disallowed_domains = getattr(spider, 'disallowed_domains', None)
        if not disallowed_domains:
            return None # allow all by default
        url_pattern = re.compile("^https?://.*$")
        for domain in disallowed_domains:
            if url_pattern.match(domain):
                warnings.warn("disallowed_domains accepts only domains, not URLs. Ignoring URL entry %s in disallowed_domains." % domain, URLWarning)

        regex = r'^(.*\.)?(%s)$' % '|'.join(re.escape(d) for d in disallowed_domains if d is not None)
        return re.compile(regex)

    def spider_opened(self, spider): # type: ignore
        self.host_regex = self.get_host_regex(spider)
        self.domains_seen = set() # type: ignore


class URLWarning(Warning):
    pass

