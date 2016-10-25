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
        i['title'] = response.xpath('//li[contains(@class,"title")]/text()').extract()
        i['url'] = response.url
        i['content']  = response.xpath('//ul[contains(@id,"content")]/div/p').extract()
        i['update_date'] =response.xpath(u'//span[contains(text(),"发布日期")]/text()').extract()[0]
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
