#coding=utf8
#!/usr/bin/python

import scrapy
from study.items import StudyItem


class Study03Spider(scrapy.Spider):
	name = 'study03'
	allowed_domains = ['study.03.demo']
	
	#用 start_requests() 替换 start_urls 列表
	def start_requests(self):
		yield scrapy.Request("http://www.baidu.com" , self.parse)
		yield scrapy.Request("http://www.pgzhe.com" , self.parse)

	#定义 parse  （默认）回调方法
	def parse(self , response):
		for h3 in response.xpath("//h3").extract():
			yield StudyItem(title=h3)

		for url in response.xpath("//a/@href").extract():
			yield scrapy.Request(url , callback=self.parse)
