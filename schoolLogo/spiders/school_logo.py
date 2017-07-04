import scrapy

from ..items import SchoollogoItem

from scrapy.crawler import CrawlerProcess
import os
class SchoollogoSpider(scrapy.Spider):
	name="schoolLogo"
	# url_list=[i for i in range(1,200)]
	# url_list[0]="http://school.liuxue360.com/us/list.html"
	# for x in range(1,199):
	# 	y=str(x)
	# 	url_list[x]="http://school.liuxue360.com/us/list-"+y+".html"
	# start_urls=["http://meiguo.liuxue86.com/school/"]
	# def parse(self,response):
	# 	sl=SchoollogoItem()
	# 	school_name=response.xpath(".//*[@class='sousuo_new clearfix']/div/div/a/text()").extract()
	# 	school_logo=response.xpath(".//*[@class='sousuo_new clearfix']/div/div/a/@href").extract()
	# 	for i,j in zip(school_name,school_logo):
	# 		sl["school"]=i
	# 		sl["images_url"]=j
	# 		yield sl
	start_urls=['http://www.llss.me/wp/']
	def parse(self,response):
		item=SchoollogoItem()
		item['image_urls']=response.xpath(".//*[@id='content']/article/div/p/img/@src").extract()
		yield item
		new_url= response.xpath(".//*[@id='wp_page_numbers']/ul/li[last()]/a/@href").extract()[0] #翻页
		#new_url= response.xpath(".//*[@id='wp_page_numbers']/ul/li/a/@href").extract_last() #或者
		if new_url:
			print(new_url)
			yield scrapy.Request(new_url,callback=self.parse)
			