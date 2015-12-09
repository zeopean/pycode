#coding=utf8
#!/usr/bin/python 

import scrapy 
from study.items import StudyItem

class Study01Spider(scrapy.Spider):
	name = 'study01'
	allowed_domains = ['study01.demo']
	start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

	def parse(self , response):
		for sel in response.xpath("//ul/li"):
			item = StudyItem()
			item['title']	= sel.xpath('a/text()').extract()
			item['link']  	= sel.xpath('a/@href').extract()
			item['desc'] 	= sel.xpath('text()').extract()
			yield item
