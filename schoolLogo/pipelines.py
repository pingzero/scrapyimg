# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class SchoollogoPipeline(object):
	def open_spider(self,spider):
		self.con=pymysql.Connect(user='root',password='root',db='test',charset='UTF8')
		self.cu=self.con.cursor()
	def process_item(self, item, spider):
		school=item['school']
		images=item['images_url']
		insert_sql='replace into school_logo (school,images_url) values(%s,%s)'
		value=[school,images]
		self.cu.execute(insert_sql,value)
		self.con.commit()
		return item
	def spider_close(self,spider):
		self.con.close()
