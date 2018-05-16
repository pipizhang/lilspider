# -*- coding: utf-8 -*-
import random
import scrapy
from ..agents import AGENTS

class UserAgentMiddleware(object):

    def process_request(self, request: scrapy.http.Request, spider: scrapy.spiders.Spider) -> None:
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent

