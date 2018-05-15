# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from baidu.spiders.search_spider import SearchSpider

if __name__ == "__main__":
  # get settings
  settings = get_project_settings()
  process = CrawlerProcess(settings=settings)

  # add mutiple spider
  process.crawl(SearchSpider)

  # start crawler
  process.start()
