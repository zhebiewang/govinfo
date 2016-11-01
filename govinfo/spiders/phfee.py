# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from govinfo.items import PhfeeItem


class PhfeeSpider(CrawlSpider):
    name = 'phfee'
    allowed_domains = ['nbgjj.com']
    start_urls = ['http://www.nbgjj.com/index.jhtml']

    rules = (
        Rule(LinkExtractor(allow=r'tzgg/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = PhfeeItem()
        i['title'] = self.get_title(response)
        i['url'] = self.get_url(response)
        i['content']  = self.get_content(response)
        i['update_date'] = self.get_update_dt(response)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def get_title(self, response):

        title = response.xpath('//li[contains(@class,"title")]/text()').extract()[0]
        return title.encode('utf-8')

    def get_url(self, response):
        return response.url

    def get_content(self, response):
        content_list  = response.xpath('//ul[contains(@id,"content")]/div/p').extract()
        content = ''.join(c.encode('utf-8') for c in content_list)  
        return content


    def get_update_dt(self, response):
        udpate_date = response.xpath(u'//span[contains(text(),"发布日期")]/text()').extract()[0]

        return udpate_date[5:].encode('utf-8')
        
