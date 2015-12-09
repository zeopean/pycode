# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.pgzhe.com"]
    start_urls = (
        'http://www.www.pgzhe.com/',
    )

    def parse(self, response):
        pass
