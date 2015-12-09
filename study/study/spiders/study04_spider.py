# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from study.items import StudyItem


class Study04SpiderPySpider(CrawlSpider):
    name = 'study04'
    allowed_domains = ['baiduticai']
    start_urls = ['http://baidu.lecai.com/']

    rules = (
        Rule(LinkExtractor(allow=r'item\.php'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
	sel.logger.info("hello , this is an item page! %s" , response.url)

        item  = scrapy.Item()
	item['title'] = response.xpath('//ul[@class="news-bar-list"]/li/a/text()').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
