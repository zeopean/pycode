#coding=utf8
#!/usr/bin/python

from scrapy.spiders import XMLFeedSpider
#from study.items import XmlItem


class XmlDemoSpider(XMLFeedSpider):
	name = "xmlDemo"
#	allowed_domains = ['www.baidu.com']
	#start_urls 	= ['htt:	
