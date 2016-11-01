# -*- coding: utf-8 -*-
import MySQLdb

class SQLPipeline(object):

	def open_spider(self, spider):

		self.connection = MySQLdb.connect(user='root', passwd='root', db='govdb', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.connection.cursor()

		pass

	def close_spider(self, spider):

		self.cursor.close()
		self.connection.commit()
		self.connection.close()

		pass


	def process_item(self, item, spider):

		self.cursor.execute("insert into phfee (title, content, url, update_dt) values ( %s , %s, %s, %s)", (item['title'], item['content'], item['url'], item['update_date']))
	
		return item