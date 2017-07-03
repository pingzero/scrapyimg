import scrapy

from ..items import SchoollogoItem

class SchoollogoSpider(scrapy.Spider):
	name="schoolLogo"
	url_list=[i for i in range(1,200)]
	url_list[0]="http://school.liuxue360.com/us/list.html"
	for x in range(1,199):
		y=str(x)
		url_list[x]="http://school.liuxue360.com/us/list-"+y+".html"
	start_urls=["http://meiguo.liuxue86.com/school/"]
	def parse(self,response):
		sl=SchoollogoItem()
		school_name=response.xpath(".//*[@class='sousuo_new clearfix']/div/div/a/text()").extract()
		school_logo=response.xpath(".//*[@class='sousuo_new clearfix']/div/div/a/@href").extract()
		for i,j in zip(school_name,school_logo):
			sl["school"]=i
			sl["images_url"]=j
			yield sl