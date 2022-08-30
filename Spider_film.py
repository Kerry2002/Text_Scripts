#coding:utf-8
import requests
from lxml import etree
from scrapy.selector import Selector

s = requests.Session()
for id in range(0,251,25):

	url = 'https://movie.douban.com/top250/?start-'+str(id)
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
	r = s.get(url,headers=headers)
	r.encoding = 'utf-8'
	root = etree.HTML(r.content)
	#使用xpath解析xml
	items = root.xpath('//ol/li/div[@class="item"]')
	print (len(items))
	for item in items:
		title = item.xpath('./div[@class = "info"]//a/span[@class="title"]/text()')
		name = title[0].encode('gb2312','ignore').decode('gb2312')
		rating = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
		# play = item.xpath('.//div[@class="bd"]//p[@class=""]/text()')[0]
		print (name,rating)

# path = r"C:\Users\DM\Desktop\豆瓣.txt"
# with open(path,'wb+') as f:
# 	f.write()