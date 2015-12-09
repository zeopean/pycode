#!/usr/bin/python3

from collections import namedtuple
webs = [
	('sohu','http://sohu.com', u'张朝阳'),
	('sina' , 'http://sina.com.cn' , u'王志东'),
	('163' , 'http://163.com',u'丁磊')
]

Webs = namedtuple('webs' ,['name','url','founder'])

for site in webs:
	site  = Webs._make(site)
	print(site)
