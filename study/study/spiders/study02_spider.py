# coding=utf8
# !/usr/bin/python

import scrapy
from study.items import StudyItem


class Study02Spider(scrapy.Spider):
    name = 'study02'
    allowed_domain = ['study.02.demo']
    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/"]

    def parse(self, response):

        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):

        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
