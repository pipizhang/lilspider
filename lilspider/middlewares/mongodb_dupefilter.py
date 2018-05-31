# -*- coding: utf-8 -*-
import logging
import scrapy
from scrapy.exceptions import IgnoreRequest, NotConfigured
from pymongo import errors
from pymongo.mongo_client import MongoClient

logger = logging.getLogger(__name__)

class MongoDBDupeFilterMiddleware(object):
    """A dupe filter middleware that considers item.url in MongoDB"""

    def __init__(self, settings): # type: ignore
        if settings.get('MONGODB_URI') is None:
            raise NotConfigured
        if settings.get('MONGODB_UNIQUE_KEY') != 'url':
            raise NotConfigured

    @classmethod
    def from_crawler(cls, crawler): # type: ignore
        o = cls(crawler.settings)
        return o

    def process_request(self, request: scrapy.http.Request, spider: scrapy.spiders.Spider) -> None:
        client = MongoClient(spider.settings.get('MONGODB_URI'))
        db = client[spider.settings.get('MONGODB_DATABASE')]
        collention = db[spider.settings.get('MONGODB_COLLECTION')]
        res = collention.find_one({'url': request.url})
        client.close()
        if res is not None:
            logger.info("MongoDBDupeFilter filtered request to: %(request)s", {'request': request.url}, extra={'spider': spider})
            raise IgnoreRequest()

